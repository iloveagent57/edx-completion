"""
Custom Django fields.
"""

from __future__ import unicode_literals

from django.db import models


class BigAutoField(models.AutoField):
    """
    AutoField that uses BigIntegers.

    This exists in Django as of version 1.10.
    """

    def db_type(self, connection):
        """
        The type of the field to insert into the database.
        """
        conn_module = type(connection).__module__
        if "mysql" in conn_module:
            return "bigint AUTO_INCREMENT"
        elif "postgres" in conn_module:
            return "bigserial"
        else:
            return super(BigAutoField, self).db_type(connection)

    def rel_db_type(self, connection):
        """
        The type to be used by relations pointing to this field.

        Not used until Django 1.10.
        """
        return "bigint"
