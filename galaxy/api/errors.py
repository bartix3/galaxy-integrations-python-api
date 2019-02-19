from galaxy.api.jsonrpc import ApplicationError

class UnknownError(ApplicationError):
    def __init__(self, data=None):
        super().__init__(0, "Unknown error", data)

class AuthenticationRequired(ApplicationError):
    def __init__(self, data=None):
        super().__init__(1, "Authentication required", data)

class BackendNotAvailable(ApplicationError):
    def __init__(self, data=None):
        super().__init__(2, "Backend not available", data)

class BackendTimeout(ApplicationError):
    def __init__(self, data=None):
        super().__init__(3, "Backend timed out", data)

class BackendError(ApplicationError):
    def __init__(self, data=None):
        super().__init__(4, "Backend error", data)

class InvalidCredentials(ApplicationError):
    def __init__(self, data=None):
        super().__init__(100, "Invalid credentials", data)

class NetworkError(ApplicationError):
    def __init__(self, data=None):
        super().__init__(101, "Network error", data)

class LoggedInElsewhere(ApplicationError):
    def __init__(self, data=None):
        super().__init__(102, "Logged in elsewhere", data)

class ProtocolError(ApplicationError):
    def __init__(self, data=None):
        super().__init__(103, "Protocol error", data)

class TemporaryBlocked(ApplicationError):
    def __init__(self, data=None):
        super().__init__(104, "Temporary blocked", data)

class Banned(ApplicationError):
    def __init__(self, data=None):
        super().__init__(105, "Banned", data)

class AccessDenied(ApplicationError):
    def __init__(self, data=None):
        super().__init__(106, "Access denied", data)

class ParentalControlBlock(ApplicationError):
    def __init__(self, data=None):
        super().__init__(107, "Parental control block", data)

class DeviceBlocked(ApplicationError):
    def __init__(self, data=None):
        super().__init__(108, "Device blocked", data)

class RegionBlocked(ApplicationError):
    def __init__(self, data=None):
        super().__init__(109, "Region blocked", data)

class FailedParsingManifest(ApplicationError):
    def __init__(self, data=None):
        super().__init__(200, "Failed parsing manifest", data)

class TooManyMessagesSent(ApplicationError):
    def __init__(self, data=None):
        super().__init__(300, "Too many messages sent", data)

class IncoherentLastMessage(ApplicationError):
    def __init__(self, data=None):
        super().__init__(400, "Different last message id on backend", data)

class MessageNotFound(ApplicationError):
    def __init__(self, data=None):
        super().__init__(500, "Message not found", data)