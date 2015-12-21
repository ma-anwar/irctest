import base64

from irctest import cases
from irctest.irc_utils.message_parser import Message

class RegistrationTestCase(cases.BaseServerTestCase):
    def testRegistration(self):
        self.controller.registerUser(self, 'testuser', 'mypassword')

class SaslTestCase(cases.BaseServerTestCase, cases.OptionalityHelper):
    @cases.OptionalityHelper.skipUnlessHasMechanism('PLAIN')
    def testPlain(self):
        """PLAIN authentication with correct username/password."""
        self.controller.registerUser(self, 'foo', 'sesame')
        self.controller.registerUser(self, 'jilles', 'sesame')
        self.controller.registerUser(self, 'bar', 'sesame')
        self.addClient()
        self.sendLine(1, 'CAP LS 302')
        capabilities = self.getCapLs(1)
        self.assertIn('sasl', capabilities,
                fail_msg='Does not have SASL as the controller claims.')
        if capabilities['sasl'] is not None:
            self.assertIn('PLAIN', capabilities['sasl'],
                fail_msg='Does not have PLAIN mechanism as the controller '
                'claims')
        self.sendLine(1, 'AUTHENTICATE PLAIN')
        m = self.getMessage(1, filter_pred=lambda m:m.command != 'NOTICE')
        self.assertMessageEqual(m, command='AUTHENTICATE', params=['+'],
                fail_msg='Sent “AUTHENTICATE PLAIN”, server should have '
                'replied with “AUTHENTICATE +”, but instead sent: {msg}')
        self.sendLine(1, 'AUTHENTICATE amlsbGVzAGppbGxlcwBzZXNhbWU=')
        m = self.getMessage(1, filter_pred=lambda m:m.command != 'NOTICE')
        self.assertMessageEqual(m, command='900',
                fail_msg='Did not send 900 after correct SASL authentication.')
        self.assertEqual(m.params[2], 'jilles', m,
                fail_msg='900 should contain the account name as 3rd argument '
                '({expects}), not {got}: {msg}')

    @cases.OptionalityHelper.skipUnlessHasSasl
    def testMechanismNotAvailable(self):
        """“If authentication fails, a 904 or 905 numeric will be sent”
        -- <http://ircv3.net/specs/extensions/sasl-3.1.html#the-authenticate-command>
        """
        self.controller.registerUser(self, 'jilles', 'sesame')
        self.addClient()
        self.sendLine(1, 'CAP LS 302')
        capabilities = self.getCapLs(1)
        self.assertIn('sasl', capabilities,
                fail_msg='Does not have SASL as the controller claims.')
        self.sendLine(1, 'AUTHENTICATE FOO')
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='904',
                fail_msg='Did not reply with 904 to “AUTHENTICATE FOO”: {msg}')

    @cases.OptionalityHelper.skipUnlessHasMechanism('PLAIN')
    def testPlainLarge(self):
        """Test the client splits large AUTHENTICATE messages whose payload
        is not a multiple of 400.
        <http://ircv3.net/specs/extensions/sasl-3.1.html#the-authenticate-command>
        """
        self.controller.registerUser(self, 'foo', 'bar'*100)
        authstring = base64.b64encode(b'\x00'.join(
            [b'foo', b'foo', b'bar'*100])).decode()
        self.addClient()
        self.sendLine(1, 'CAP LS 302')
        capabilities = self.getCapLs(1)
        self.assertIn('sasl', capabilities,
                fail_msg='Does not have SASL as the controller claims.')
        if capabilities['sasl'] is not None:
            self.assertIn('PLAIN', capabilities['sasl'],
                fail_msg='Does not have PLAIN mechanism as the controller '
                'claims')
        self.sendLine(1, 'AUTHENTICATE PLAIN')
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='AUTHENTICATE', params=['+'],
                fail_msg='Sent “AUTHENTICATE PLAIN”, expected '
                '“AUTHENTICATE +” as a response, but got: {msg}')
        self.sendLine(1, 'AUTHENTICATE {}'.format(authstring[0:400]))
        self.sendLine(1, 'AUTHENTICATE {}'.format(authstring[400:]))

        # TODO: may be in the other order
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='900',
                fail_msg='Expected 900 (RPL_LOGGEDIN) after successful '
                'login, but got: {msg}')
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='903',
                fail_msg='Expected 900 (RPL_LOGGEDIN) after successful '
                'login, but got: {msg}')

    # TODO: add a test for when the length of the authstring is greater than 800.
    # I don't know how to do it, because it would make the registration
    # message's length too big for it to be valid.

    @cases.OptionalityHelper.skipUnlessHasMechanism('PLAIN')
    def testPlainLargeEquals400(self):
        """Test the client splits large AUTHENTICATE messages whose payload
        is not a multiple of 400.
        <http://ircv3.net/specs/extensions/sasl-3.1.html#the-authenticate-command>
        """
        self.controller.registerUser(self, 'foo', 'bar'*97)
        authstring = base64.b64encode(b'\x00'.join(
            [b'foo', b'foo', b'bar'*97])).decode()
        assert len(authstring) == 400, 'Bad test'
        self.addClient()
        self.sendLine(1, 'CAP LS 302')
        capabilities = self.getCapLs(1)
        self.assertIn('sasl', capabilities,
                fail_msg='Does not have SASL as the controller claims.')
        if capabilities['sasl'] is not None:
            self.assertIn('PLAIN', capabilities['sasl'],
                fail_msg='Does not have PLAIN mechanism as the controller '
                'claims')
        self.sendLine(1, 'AUTHENTICATE PLAIN')
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='AUTHENTICATE', params=['+'],
                fail_msg='Sent “AUTHENTICATE PLAIN”, expected '
                '“AUTHENTICATE +” as a response, but got: {msg}')
        self.sendLine(1, 'AUTHENTICATE {}'.format(authstring))
        self.sendLine(1, 'AUTHENTICATE +')

        # TODO: may be in the other order
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='900',
                fail_msg='Expected 900 (RPL_LOGGEDIN) after successful '
                'login, but got: {msg}')
        m = self.getRegistrationMessage(1)
        self.assertMessageEqual(m, command='903',
                fail_msg='Expected 900 (RPL_LOGGEDIN) after successful '
                'login, but got: {msg}')

    # TODO: add a test for when the length of the authstring is 800.
    # I don't know how to do it, because it would make the registration
    # message's length too big for it to be valid.
