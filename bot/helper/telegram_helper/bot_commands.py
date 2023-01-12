from bot import CMD_PERFIX
from os import environ

def getCommand(name: str, command: str):
    try:
        if len(environ[name]) == 0:
            raise KeyError
        return environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_COMMAND', f'start{CMD_PERFIX}')
        self.MirrorCommand = (
            getCommand('MIRROR_COMMAND', f'mirror{CMD_PERFIX}'),
            f'm{CMD_PERFIX}',
        )
        self.UnzipMirrorCommand = (
            getCommand('UNZIP_COMMAND', f'unzipmirror{CMD_PERFIX}'),
            f'uzm{CMD_PERFIX}',
        )
        self.ZipMirrorCommand = (
            getCommand('ZIP_COMMAND', f'zipmirror{CMD_PERFIX}'),
            f'zm{CMD_PERFIX}',
        )
        self.LeechCommand = (
            getCommand('LEECH_COMMAND', f'leech{CMD_PERFIX}'),
            f'l{CMD_PERFIX}',
        )
        self.UnzipLeechCommand = (
            getCommand('UNZIPLEECH_COMMAND', f'unzipleech{CMD_PERFIX}'),
            f'uzl{CMD_PERFIX}',
        )
        self.ZipLeechCommand = (
            getCommand('ZIPLEECH_COMMAND', f'zipleech{CMD_PERFIX}'),
            f'zl{CMD_PERFIX}',
        )
        self.CloneCommand = (
            getCommand('CLONE_COMMAND', f'clone{CMD_PERFIX}'),
            f'c{CMD_PERFIX}',
        )
        self.QbMirrorCommand = (
            getCommand('QBMIRROR_COMMAND', f'qbmirror{CMD_PERFIX}'),
            f'qm{CMD_PERFIX}',
        )
        self.QbUnzipMirrorCommand = (
            getCommand('QBUNZIP_COMMAND', f'qbunzipmirror{CMD_PERFIX}'),
            f'quzm{CMD_PERFIX}',
        )
        self.QbZipMirrorCommand = (
            getCommand('QBZIP_COMMAND', f'qbzipmirror{CMD_PERFIX}'),
            f'qzm{CMD_PERFIX}',
        )
        self.QbLeechCommand = (
            getCommand('QBLEECH_COMMAND', f'qbleech{CMD_PERFIX}'),
            f'ql{CMD_PERFIX}',
        )
        self.QbUnzipLeechCommand = (
            getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech{CMD_PERFIX}'),
            f'quzl{CMD_PERFIX}',
        )
        self.QbZipLeechCommand = (
            getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech{CMD_PERFIX}'),
            f'qzl{CMD_PERFIX}',
        )
        self.ScrapeCommand = (
            getCommand('SCRAPE_COMMAND', f'scrape{CMD_PERFIX}'),
            f'sm{CMD_PERFIX}',
        )
        self.YtdlCommand = (
            getCommand('YTDL_COMMAND', f'ytdl{CMD_PERFIX}'),
            f'y{CMD_PERFIX}',
        )
        self.YtdlZipCommand = (
            getCommand('YTDLZIP_COMMAND', f'ytdlzip{CMD_PERFIX}'),
            f'yz{CMD_PERFIX}',
        )
        self.YtdlLeechCommand = (
            getCommand('YTDLLEECH_COMMAND', f'ytdlleech{CMD_PERFIX}'),
            f'yl{CMD_PERFIX}',
        )
        self.YtdlZipLeechCommand = (
            getCommand('YTDLZIPLEECH_COMMAND', f'ytdlzipleech{CMD_PERFIX}'),
            f'yzl{CMD_PERFIX}',
        )
        self.MediaInfoCommand = (
            getCommand('MEDIAINFO_COMMAND', f'mediainfo{CMD_PERFIX}'),
            f'mi{CMD_PERFIX}',
        )
        self.UserSetCommand = (
            getCommand('USERSET_COMMAND', f'usetting{CMD_PERFIX}'),
            f'us{CMD_PERFIX}',
        )
        self.BotSetCommand = (
            getCommand('BOT_SETTING', f'bsetting{CMD_PERFIX}'),
            f'bs{CMD_PERFIX}',
        )
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel{CMD_PERFIX}')
        self.CancelAllCommand = getCommand(
            'CANCEL_ALL_COMMAND', f'cancelall{CMD_PERFIX}'
        )
        self.ListCommand = getCommand('LIST_COMMAND', f'list{CMD_PERFIX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{CMD_PERFIX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status{CMD_PERFIX}')
        self.UsersCommand = getCommand('USERS_COMMAND', f'users{CMD_PERFIX}')
        self.PaidUsersCommand = getCommand('PAID_COMMAND', f'paid{CMD_PERFIX}')
        self.AddPaidCommand = getCommand('ADDPAID_COMMAND', f'addpaid{CMD_PERFIX}')
        self.RmPaidCommand = getCommand('RMPAID_COMMAND', f'rmpaid{CMD_PERFIX}')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'authorize{CMD_PERFIX}')
        self.UnAuthorizeCommand = getCommand(
            'UNAUTH_COMMAND', f'unauthorize{CMD_PERFIX}'
        )
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'addsudo{CMD_PERFIX}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'rmsudo{CMD_PERFIX}')
        self.PingCommand = getCommand('PING_COMMAND', f'ping{CMD_PERFIX}')
        self.RestartCommand = getCommand('RESTART_COMMAND', f'restart{CMD_PERFIX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{CMD_PERFIX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{CMD_PERFIX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'log{CMD_PERFIX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'btsel{CMD_PERFIX}')
        self.SpeedCommand = (
            getCommand('SPEEDTEST_COMMAND', f'speedtest{CMD_PERFIX}'),
            f'st{CMD_PERFIX}',
        )
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{CMD_PERFIX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{CMD_PERFIX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell{CMD_PERFIX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'exechelp{CMD_PERFIX}')
        self.HashCommand = getCommand('HASH_COMMAND', f'hash{CMD_PERFIX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'rsslist{CMD_PERFIX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'rssget{CMD_PERFIX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'rsssub{CMD_PERFIX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'rssunsub{CMD_PERFIX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'rssset{CMD_PERFIX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'wayback{CMD_PERFIX}')
        self.AddleechlogCommand = getCommand(
            'ADDLEECHLOG_CMD', f'addleechlog{CMD_PERFIX}'
        )
        self.RmleechlogCommand = getCommand(
            'RMLEECHLOG_CMD', f'rmleechlog{CMD_PERFIX}'
        )
        self.EvalCommand = f'eval{CMD_PERFIX}'
        self.ExecCommand = f'exec{CMD_PERFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_PERFIX}'

BotCommands = _BotCommands()
