from apps.file.models import AbstractFileModel


class SimpleFile(AbstractFileModel):
    """
    File that has relation one-to-one which relation describe in target table not here.
    For example banner-image file which are related to a post in our blog.
    """
    pass
