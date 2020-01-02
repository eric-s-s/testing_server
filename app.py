
from flask import Flask, request, logging

app = Flask(__name__)
logger = logging.create_logger(app)

@app.route("/test", methods=['POST'])
def test_thing():
    # data = request.data
    # logger.warn(str(data))
    logger.warn(request.headers)
    logger.warn(request.mimetype)
    logger.warn(request.files)
    # file = request.files['file']
    # logger.warn("filename: {}".format(file.filename))
    # logger.warn("content-type: {}".format(request.content_type))

    # logger.warn(request.content_length)
    # logger.warn(request.content_encoding)
    # logger.warn(request.data)
    # logger.warn(request.form)
    # logger.warn(request.form_data_parser_class)
    # logger.warn(request.form)
    # logger.warn(request.args)
    # request.files['file'].save('delme')
    with open('raw', 'w') as f:
        f.write(str(request.get_data()))
        f.write(request.mimetype)
    return "ok"

if __name__ == '__main__':
    app.run()
