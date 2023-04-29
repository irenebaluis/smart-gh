from .. import *
from ethereum.middleware.sign_transaction import sign_contract, build_transaction
from fastapi import APIRouter
from ..models import user_model

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post("/add")
def register(caller, private_key, user: user_model.User):
    call_function = CONTRACT.functions.register(
        user.userAddress, user.userRole, user.email, user.isApproved
    ).build_transaction(build_transaction(caller))
    sign_contract(call_function, private_key)
    return call_function


@router.get("/is_admin/{userID}")
async def is_admin(user_id: int):
    user = CONTRACT.functions.isAdmin(user_id).call()
    return user


@router.get("/get_user/{userID}")
async def get_user(user_id: int):
    user = CONTRACT.functions.getUser(user_id).call()
    return user


@router.get("/get_users")
async def get_user():
    user = CONTRACT.functions.getAllUsers().call()
    return user


@router.delete("/delete/{userID}")
def register(caller, private_key, user_id: int):
    call_function = CONTRACT.functions.deleteUser(user_id).build_transaction(build_transaction(caller))
    sign_contract(call_function, private_key)
    return call_function


@router.post("/approve/{userID}")
def approve(caller, private_key, user_id: int):
    call_function = CONTRACT.functions.approveUser(user_id).build_transaction(build_transaction(caller))
    sign_contract(call_function, private_key)
    return call_function
