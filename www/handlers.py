from coroweb import get

from models import User

' url handlers '

@get('/')
async def index(request):
    users = await User.findAll()
    return  {
        '__template__': 'test.html',
        'users': users
    }