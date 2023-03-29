class Connection:
    hostname: str
    remote_user: str
    named_passwd: str

    def __init__(
            self,
            hostname: str,
            remote_user: str,
            named_passwd: str
    ):
        self.hostname = hostname
        self.remote_user = remote_user
        self.named_passwd = named_passwd

    def sshpass(self) -> str:
        return f"sshpass -p ${self.named_passwd}_{self.remote_user} ssh {self.remote_user}@{self.hostname}"

    def to_json(self) -> dict:
        return {
            "hostname": self.hostname,
            "remote_user": self.remote_user,
            "named_passwd": self.named_passwd
        }

    def __str__(self) -> str:
        return f"{self.remote_user}@{self.hostname}"
