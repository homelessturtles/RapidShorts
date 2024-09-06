import firebase_admin
from firebase_admin import firestore, initialize_app, credentials, auth, storage


cred = credentials.Certificate("rapidshorts-firebase.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'rapidshorts-b27d3.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()

firebase_auth = auth