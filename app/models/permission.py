from app import db 
class Permission(db.Model):
    __tablename__ = "flasky_permission"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    permission_type = db.Column(db.String(50), nullable = False)

    def __str__(self):
        return "Permission: {}".format(self.permission_type) 


class Menu(db.Model):
    __tablename__ = "flasky_menu"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    url = db.Column(db.String(500))
    parent_id = db.Column(db.Integer)

    def __str__(self):
        return "Menu: " + self.name
    
class PermissionAndMenu(db.Model):
    __tablename__ = "flasky_permission_menu"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    permission_id = db.Column(db.Integer, nullable = False)
    menu_id = db.Column(db.Integer, nullable = False)


class Operation(db.Model):
    __tablename__ = "flasky_operation"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    code = db.Column(db.String(30))
    prefix_url = db.Column(db.String(300))
    parent_id = db.Column(db.Integer)

class PermissionAndOperation(db.Model):
    __tablename__ = "flasky_permission_operation"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    permission_id = db.Column(db.Integer, nullable = False)
    operation_id = db.Column(db.Integer, nullable = False)


class PermissionAndRole(db.Model):
    __tablename__ = "flasky_permission_role"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    permission_id = db.Column(db.Integer, nullable = False)
    role_id = db.Column(db.Integer, nullable = False)


class OperationLog(db.Model):
    __tablename__ = "flasky_operation_log"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    operation_id = db.Column(db.Integer, nullable = False)
    operation_content = db.Column(db.String(500))
    user_id = db.Column(db.Integer, nullable = False)
    operation_time = db.Column(db.Date)
