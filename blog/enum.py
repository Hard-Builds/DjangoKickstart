import enum


class PostStatusEnum(enum.Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
