# Copyright (c) 2012-2014 Jeremy Latt
# Copyright (c) 2014-2015 Edmund Huber
# Copyright (c) 2016-2017 Daniel Oaks <daniel@danieloaks.net>
# released under the MIT license

# These numerics have been retrieved from:
#   http://defs.ircdocs.horse/ and http://modern.ircdocs.horse/

# They're intended to represent a relatively-standard cross-section of the IRC
# server ecosystem out there. Custom numerics will be marked as such.

RPL_WELCOME                     = "001"
RPL_YOURHOST                    = "002"
RPL_CREATED                     = "003"
RPL_MYINFO                      = "004"
RPL_ISUPPORT                    = "005"
RPL_SNOMASKIS                   = "008"
RPL_BOUNCE                      = "010"
RPL_TRACELINK                   = "200"
RPL_TRACECONNECTING             = "201"
RPL_TRACEHANDSHAKE              = "202"
RPL_TRACEUNKNOWN                = "203"
RPL_TRACEOPERATOR               = "204"
RPL_TRACEUSER                   = "205"
RPL_TRACESERVER                 = "206"
RPL_TRACESERVICE                = "207"
RPL_TRACENEWTYPE                = "208"
RPL_TRACECLASS                  = "209"
RPL_TRACERECONNECT              = "210"
RPL_STATSLINKINFO               = "211"
RPL_STATSCOMMANDS               = "212"
RPL_ENDOFSTATS                  = "219"
RPL_UMODEIS                     = "221"
RPL_SERVLIST                    = "234"
RPL_SERVLISTEND                 = "235"
RPL_STATSUPTIME                 = "242"
RPL_STATSOLINE                  = "243"
RPL_LUSERCLIENT                 = "251"
RPL_LUSEROP                     = "252"
RPL_LUSERUNKNOWN                = "253"
RPL_LUSERCHANNELS               = "254"
RPL_LUSERME                     = "255"
RPL_ADMINME                     = "256"
RPL_ADMINLOC1                   = "257"
RPL_ADMINLOC2                   = "258"
RPL_ADMINEMAIL                  = "259"
RPL_TRACELOG                    = "261"
RPL_TRACEEND                    = "262"
RPL_TRYAGAIN                    = "263"
RPL_WHOISCERTFP                 = "276"
RPL_AWAY                        = "301"
RPL_USERHOST                    = "302"
RPL_ISON                        = "303"
RPL_UNAWAY                      = "305"
RPL_NOWAWAY                     = "306"
RPL_WHOISUSER                   = "311"
RPL_WHOISSERVER                 = "312"
RPL_WHOISOPERATOR               = "313"
RPL_WHOWASUSER                  = "314"
RPL_ENDOFWHO                    = "315"
RPL_WHOISIDLE                   = "317"
RPL_ENDOFWHOIS                  = "318"
RPL_WHOISCHANNELS               = "319"
RPL_LIST                        = "322"
RPL_LISTEND                     = "323"
RPL_CHANNELMODEIS               = "324"
RPL_UNIQOPIS                    = "325"
RPL_CHANNELCREATED              = "329"
RPL_WHOISACCOUNT                = "330"
RPL_NOTOPIC                     = "331"
RPL_TOPIC                       = "332"
RPL_TOPICTIME                   = "333"
RPL_WHOISBOT                    = "335"
RPL_WHOISACTUALLY               = "338"
RPL_INVITING                    = "341"
RPL_SUMMONING                   = "342"
RPL_INVITELIST                  = "346"
RPL_ENDOFINVITELIST             = "347"
RPL_EXCEPTLIST                  = "348"
RPL_ENDOFEXCEPTLIST             = "349"
RPL_VERSION                     = "351"
RPL_WHOREPLY                    = "352"
RPL_NAMREPLY                    = "353"
RPL_LINKS                       = "364"
RPL_ENDOFLINKS                  = "365"
RPL_ENDOFNAMES                  = "366"
RPL_BANLIST                     = "367"
RPL_ENDOFBANLIST                = "368"
RPL_ENDOFWHOWAS                 = "369"
RPL_INFO                        = "371"
RPL_MOTD                        = "372"
RPL_ENDOFINFO                   = "374"
RPL_MOTDSTART                   = "375"
RPL_ENDOFMOTD                   = "376"
RPL_YOUREOPER                   = "381"
RPL_REHASHING                   = "382"
RPL_YOURESERVICE                = "383"
RPL_TIME                        = "391"
RPL_USERSSTART                  = "392"
RPL_USERS                       = "393"
RPL_ENDOFUSERS                  = "394"
RPL_NOUSERS                     = "395"
ERR_UNKNOWNERROR                = "400"
ERR_NOSUCHNICK                  = "401"
ERR_NOSUCHSERVER                = "402"
ERR_NOSUCHCHANNEL               = "403"
ERR_CANNOTSENDTOCHAN            = "404"
ERR_TOOMANYCHANNELS             = "405"
ERR_WASNOSUCHNICK               = "406"
ERR_TOOMANYTARGETS              = "407"
ERR_NOSUCHSERVICE               = "408"
ERR_NOORIGIN                    = "409"
ERR_INVALIDCAPCMD               = "410"
ERR_NORECIPIENT                 = "411"
ERR_NOTEXTTOSEND                = "412"
ERR_NOTOPLEVEL                  = "413"
ERR_WILDTOPLEVEL                = "414"
ERR_BADMASK                     = "415"
ERR_INPUTTOOLONG                = "417"
ERR_UNKNOWNCOMMAND              = "421"
ERR_NOMOTD                      = "422"
ERR_NOADMININFO                 = "423"
ERR_FILEERROR                   = "424"
ERR_NONICKNAMEGIVEN             = "431"
ERR_ERRONEUSNICKNAME            = "432"
ERR_NICKNAMEINUSE               = "433"
ERR_NICKCOLLISION               = "436"
ERR_UNAVAILRESOURCE             = "437"
ERR_REG_UNAVAILABLE             = "440"
ERR_USERNOTINCHANNEL            = "441"
ERR_NOTONCHANNEL                = "442"
ERR_USERONCHANNEL               = "443"
ERR_NOLOGIN                     = "444"
ERR_SUMMONDISABLED              = "445"
ERR_USERSDISABLED               = "446"
ERR_NOTREGISTERED               = "451"
ERR_NEEDMOREPARAMS              = "461"
ERR_ALREADYREGISTRED            = "462"
ERR_NOPERMFORHOST               = "463"
ERR_PASSWDMISMATCH              = "464"
ERR_YOUREBANNEDCREEP            = "465"
ERR_YOUWILLBEBANNED             = "466"
ERR_KEYSET                      = "467"
ERR_INVALIDUSERNAME             = "468"
ERR_CHANNELISFULL               = "471"
ERR_UNKNOWNMODE                 = "472"
ERR_INVITEONLYCHAN              = "473"
ERR_BANNEDFROMCHAN              = "474"
ERR_BADCHANNELKEY               = "475"
ERR_BADCHANMASK                 = "476"
ERR_NOCHANMODES                 = "477"
ERR_BANLISTFULL                 = "478"
ERR_NOPRIVILEGES                = "481"
ERR_CHANOPRIVSNEEDED            = "482"
ERR_CANTKILLSERVER              = "483"
ERR_RESTRICTED                  = "484"
ERR_UNIQOPPRIVSNEEDED           = "485"
ERR_NOOPERHOST                  = "491"
ERR_UMODEUNKNOWNFLAG            = "501"
ERR_USERSDONTMATCH              = "502"
ERR_HELPNOTFOUND                = "524"
ERR_CANNOTSENDRP                = "573"
RPL_WHOISSECURE                 = "671"
RPL_YOURLANGUAGESARE            = "687"
RPL_WHOISLANGUAGE               = "690"
ERR_INVALIDMODEPARAM            = "696"
RPL_HELPSTART                   = "704"
RPL_HELPTXT                     = "705"
RPL_ENDOFHELP                   = "706"
ERR_NOPRIVS                     = "723"
RPL_MONONLINE                   = "730"
RPL_MONOFFLINE                  = "731"
RPL_MONLIST                     = "732"
RPL_ENDOFMONLIST                = "733"
ERR_MONLISTFULL                 = "734"
RPL_LOGGEDIN                    = "900"
RPL_LOGGEDOUT                   = "901"
ERR_NICKLOCKED                  = "902"
RPL_SASLSUCCESS                 = "903"
ERR_SASLFAIL                    = "904"
ERR_SASLTOOLONG                 = "905"
ERR_SASLABORTED                 = "906"
ERR_SASLALREADY                 = "907"
RPL_SASLMECHS                   = "908"
RPL_REGISTRATION_SUCCESS        = "920"
ERR_ACCOUNT_ALREADY_EXISTS      = "921"
ERR_REG_UNSPECIFIED_ERROR       = "922"
RPL_VERIFYSUCCESS               = "923"
ERR_ACCOUNT_ALREADY_VERIFIED    = "924"
ERR_ACCOUNT_INVALID_VERIFY_CODE = "925"
RPL_REG_VERIFICATION_REQUIRED   = "927"
ERR_REG_INVALID_CRED_TYPE       = "928"
ERR_REG_INVALID_CALLBACK        = "929"
ERR_TOOMANYLANGUAGES            = "981"
ERR_NOLANGUAGE                  = "982"
