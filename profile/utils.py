from uuid import uuid4

import python_avatars as pa

MBTI = [
    "ISTJ",
    "ISFJ",
    "INFJ",
    "INTJ",
    "ISTP",
    "ISFP",
    "INFP",
    "INTP",
    "ESTP",
    "ESFP",
    "ENFP",
    "ENTP",
    "ESTJ",
    "ESFJ",
    "ENFJ",
    "ENTJ",
]


def random_avatar():
    avatar = pa.Avatar.random()
    filename = f"assets/avatar_{uuid4()}.svg"
    avatar.render(filename)

    return filename
