class WrdRouter:
    """
    A router to control all database operations on models in the
    projects application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read word models go to dictionary.
        """
        if model._meta.app_label == 'word':
            return 'dictionary'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write word models go to dictionary.
        """
        if model._meta.app_label == 'word':
            return 'dictionary'
        return None

    # Not working with relations so this shouldn't be necessary
    
    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the projects app is involved.
    #     """
    #     if obj1._meta.app_label == 'project' or \
    #        obj2._meta.app_label == 'project':
    #        return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the word app only appears in the 'dictionary'
        database.
        """
        if app_label == 'project':
            return db == 'dictionary'
        return None