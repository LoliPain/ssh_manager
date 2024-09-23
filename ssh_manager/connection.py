from typing import Optional

from pydantic import BaseModel, field_validator


class StoredConnection(BaseModel):
    """Single element from store as python object

    """
    hostname: str
    remote_user: str
    named_passwd: Optional[str] = None
    key_file: Optional[str] = None

    @field_validator('*')
    @classmethod
    def prohibit_blank_string(cls, _):
        """Stricter validation for models, that prohibits empty required string strings
        """
        if len(_) != 0:
            return _
        raise ValueError


class Connection:
    """Basic stored connection

    """

    def __init__(
            self,
            hostname: str,
            remote_user: str,
            named_passwd: Optional[str] = None,
            key_file: Optional[str] = None

    ):
        """Create a new stored connection

        :param hostname: Remote hostname or IP
        :param remote_user: User on remote machine
        :param named_passwd: First part of env var password that declares a shortened hostname,
                            is required if no key_file given
                            (eg *chkitty* for $chkitty_sweety)
        :param key_file: Stringified path to key file, mutually exclusive for named_passwd
                            (eg *chkitty* for $chkitty_sweety)
        """
        self.hostname = hostname
        self.remote_user = remote_user

        if (not named_passwd and not key_file) or (named_passwd and key_file):
            raise Exception("Either named_passwd or key_file field are required")
        self.named_passwd = named_passwd
        self.key_file = key_file

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
        """Validate instance using :StoredConnection model

        :return: :StoredConnection model instance
        """
        model_fields = {
            "hostname": self.hostname,
            "remote_user": self.remote_user,
        }
        if self.named_passwd:
            model_fields["named_passwd"] = self.named_passwd
        elif self.key_file:
            model_fields["key_file"] = self.key_file
        return StoredConnection.model_validate(model_fields)

    def __str__(self) -> str:
        """User-readable entry

        :return: user@host
        """
        return f"{self.remote_user}@{self.hostname}"
