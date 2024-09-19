from pydantic import BaseModel


class StoredConnection(BaseModel):
    """Single element from store as python object

    """
    hostname: str
    remote_user: str
    named_passwd: str


class Connection:
    """Basic stored connection

    """
    hostname: str
    remote_user: str
    named_passwd: str

    def __init__(
            self,
            hostname: str,
            remote_user: str,
            named_passwd: str
    ):
        """Create a new stored connection

        :param hostname: Remote hostname or IP
        :param remote_user: User on remote machine
        :param named_passwd: First part of env var password that declares a shortened hostname
                            (eg *chkitty* for $chkitty_sweety)
        """
        self.hostname = hostname
        self.remote_user = remote_user
        self.named_passwd = named_passwd

    def env_passwd(self) -> str:
        """Return a specified env var for selected connection

        :return: $server_user like variable
        """
        return f"{self.named_passwd}_{self.remote_user}"

    def sshpass(self) -> str:
        """Returns a sshpass prepared action

        :return: sshpass -p passwd ssh user@host
        """
        return f"sshpass -p ${self.env_passwd()} ssh {self.remote_user}@{self.hostname}"

    def to_model(self) -> StoredConnection:
        """Prepare instance for JSON dumping

        :return: JSON-compatible dict
        """
        return StoredConnection.model_validate({
            "hostname": self.hostname,
            "remote_user": self.remote_user,
            "named_passwd": self.named_passwd
        })

    def __str__(self) -> str:
        """User-readable entry

        :return: user@host
        """
        return f"{self.remote_user}@{self.hostname}"
