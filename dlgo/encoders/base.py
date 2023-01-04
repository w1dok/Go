import importlib

class Encoder:
    def name(self):
        raise NotImplementedError()

    def encoder(self, game_state):
        raise NotImplementedError()

    def encoder_point(self, point):
        raise NotImplementedError()

    def decoder_point_index(self, index):
        raise NotImplementedError()

    def num_points(self):
        raise NotImplementedError()

    def shape(self):
        raise NotImplementedError()

    def get_encoder_by_name(name, board_size):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        module = importlib.import_module('dlgo.encoders.' + name)
        constructor = getattr(module, 'create')
        return constructor(board_size)