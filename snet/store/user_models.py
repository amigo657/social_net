import re
import asyncio
from random import random
from hashlib import sha3_256
from tortoise import models, fields, signals, validators
from ._regex_value import RFC5322


class User(models.Model):
    id = fields.BigIntField(pk = True)
    full_name = fields.CharField(max_length = 256, index = True)
    email = fields.CharField(
        max_lenght = 100,
        unique = True,
        index = True,
        validators = [validators.RegexValidator(RFC5322, flags = re.IGNORECASE)],
    )
    password = fields.CharField(max_length = 128, unique = True)
    is_active = fields.BooleanField(default = False)

    class Meta:
        table = "user"

    def __str__(self):
        return self.email

    async def is_correct(self, password):
        pass_hash = self.password[:64]
        salt = self.password[64:]
        check_hash = sha3_256(password.encode("utf-8")).hexdigest()
        value = "".join([a + b for a, b in zip(salt, check_hash)]).encode("utf-8")
        await asyncio.sleep(3)
        return sha3_256(value).hexdigest() == pass_hash

@signals.pre_save(User)
async def hide_password(sender, instance, using_db, update_fields):
    if update_fields is None or "password" in update_fields:
        pass_hash = sha3_256(instance.password.encode("utf-8")).hexdigest()
        salt = sha3_256((random()).hex().encode("utf-8")).hexdigest()
        value = "".join([a + b for a, b in zip(salt, pass_hash)]).encode("utf-8")
        instance.password = sha3_256(value).hexdigest() + salt



# class EmailValidator(validators.Validator):
#     def __init__(
#         self,
#         regex: Optional[str] = None,
#         flags: Optional[Union[int, re.RegexFlag]] = 0,
#     ):
#         if regex is None:
#             regex = RFC5322
#         self._regex = re.compile(regex, flags)

#     def __call__(self, value):
#         if not self._regex.match(value):
#             raise ValidationError(
#                 f"Value '{value}' does not match regex '{self._regex.pattern}'"
#     )