from dataclasses import dataclass


@dataclass
class ApplicationError(Exception):
    @property
    def message(self):
        return "An application error occurred"
