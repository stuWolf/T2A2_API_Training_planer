from main import db
from flask import Blueprint, request, abort, jsonify
from datetime import date
from model.models import Progres, User
from schema.schemas import progres_schema, progresses_schema
from flask_jwt_extended import  jwt_required, get_jwt_identity



progres = Blueprint('progresses', __name__, url_prefix="/progresses")



# get progresses of logged in user
@progres.get("/")
@jwt_required()
def get_progresses():
    user_id = get_jwt_identity()
    progresses = Progres.query.filter_by(user_id=user_id).all()

    if not progresses:
        return abort(401, description="you have no progres record created yet")

    return progresses_schema.dump(progresses)




# print progres of a speific id
@progres.get("/<int:id>")
def get_progres(id):
    progres = Progres.query.get(id)

    if not progres:
        return abort(400, description=f"A progres with id { id } doesn't exist")


    return progres_schema.dump(progres)


# Create new progres with the user id of logged in user
@progres.post("/")
@jwt_required()
def create_progres():
    user_id = get_jwt_identity()

    # load progres fields from json
    try:
        progres_fields = progres_schema.load(request.json)
        # test if progres name is provided
        progres_name = progres_fields["progres_name"]
        if not progres_name:
            return abort(400, description=f"The progres needs a name")
        # test if progres name is provided
        # filter blanks
        progres_name= progres_name.strip().replace(" ", "")
        progres = Progres.query.filter_by(progres_name=progres_name).first()
        if progres:
             return abort(400, description=f"A progres with the name {progres_name} already exists")
        # # create new progres object
        progres = Progres(**progres_fields)
    except Exception as e:
        return jsonify(message= f'missing or incorrect key: {e} ')
    else:
        # progres.progres_name = progres_name
        progres.date = date.today()
        progres.user_id = user_id
        progres.progres_name = progres_name
        db.session.add(progres)
        db.session.commit()
        
        # print(result)
        return progres_schema.dump(progres)
        # return jsonify({'_comment': result,"progres_name":progres.progres_name, "body_region": progres.body_region, "level": progres.level, "progres": progres.progres})


# Delete progres (of logged in user )

@progres.delete("/<string:progres_name>")
@jwt_required()
def delete_progres(progres_name):
    #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    # get whole user record
    user = User.query.get(user_id)

    progres = Progres.query.get(user_id)
    #Test if progress under the name of operator exist
    if not progres:
        return abort(401, description="you have no progres record created yet")
    #Test if progress with this name exist
# get the progres
    progres = Progres.query.filter_by(progres_name=progres_name).first()
    if not progres:
        return abort(401, description=f"a progres with the id { progres_name} does not exist")
    
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == progres.user_id)):
        return abort(401, description="You can only delete your own progress or need to be an admin")
   
    
    #Delete the progres from the database and commit
    db.session.delete(progres)
    db.session.commit()
    #return the progres in the response
    return jsonify({"progres_user":progres.user_id, "progres_name": progres.progres_name, '_comment': "deleted:"})

# Amend progres of logged in user

@progres.put("/update/<string:progres_name>")
@jwt_required()
def update_progres(progres_name):
   
   #get the operator id invoking get_jwt_identity and find it in the DB
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    # find the progres, test if it exists
    print(user_id)
    progres = Progres.query.get(user_id)
    #Test if progress under the name of operator exist
    if not progres:
        return abort(401, description="you have no progres record created yet")
   
    # Stop the request if the user is not an admin or tries to edit someone elses card
    if not (user.admin or  (user_id == progres.user_id)):
        return abort(401, description="You can only edit your own progress or need to be an admin")

     # get the progres
   
    progres_old = Progres.query.filter_by(progres_name=progres_name).first()
    if not progres_old:
        return jsonify(message= f"a progres with the name '{progres_name}' does not exist"), 400

    try:
        # load progres fields from json
        progres_fields = progres_schema.load(request.json)
        new_name = progres_fields["progres_name"]
    # if a progres with the new name exists and the current progres has not 
        # check if any progres except the current one has that progres_name
        progres = Progres.query.filter_by(progres_name=new_name).first()
        if progres and not (progres_old.progres_name == new_name):
        # if  not progres_old.name == progres_name:
            return abort(400, description=f"you can not use the name '{new_name}',it already exists")
        
    #     # finally update progres
        progres = Progres.query.filter_by(progres_name=progres_name).first()
        # here first() is OK because progres name is unique
        # progres = Progres(**progres_fields)
        progres.progres_name = new_name
        progres.weight = progres_fields["weight"]
        progres.mid_arm = progres_fields["mid_arm"]
        progres.waist = progres_fields["waist"]
        progres.chest = progres_fields["chest"]
        progres.hip = progres_fields["hip"]
        progres.test_score = progres_fields["test_score"]
        progres.date = date.today()
    except Exception as e:
        return jsonify(message= f'missing or incorrect key: {e} ')
    else:
    # db.session.add(progres) ??

        # progres.user_id = user_id
        db.session.commit()
        # return jsonify({"user":user.email, "progres_name": progres.name, "progres_id": progres.id, '_comment': "updated:"})
        return progres_schema.dump(progres)



