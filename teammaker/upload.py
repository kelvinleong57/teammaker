from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['csv', 'txt'])

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        return False

    file = request.files['file']
    if file.filename == '':
        return False

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        return True

    return False