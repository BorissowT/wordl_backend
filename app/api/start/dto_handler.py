""" dto_handler.py """
from app.api.base_impl.dto_base import DTOHandlerBase
from app.api.start.schema import StartResponseSchema, StartRequestSchema

from flask import request


class StartDTOHandler(DTOHandlerBase):
    """This a data transfer abstraction layer. It's responsible for proper
     data validation, serialization and deserialization.

    """

    response_schema = StartResponseSchema()
    request_schema = StartRequestSchema()

    @classmethod
    def create_item(cls):
        """Validate input data and return encrypted id or raise validation
         error.

        :return: encrypted id
        """
        data = request.json
        model_instance = cls.request_schema.load(data)
        inserted_id = ApartmentConfigsRepository.add_item(model_instance)
        return jsonify({'inserted_id': encrypt_id(str(inserted_id))})