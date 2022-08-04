from pickle import TRUE


class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos.""" 
        self.ai_settings = ai_settings
        self.reset_stats() 
        self.game_active = False
        
    def reset_stats(self): 
        """Inicializa os dados estatísticos que podem mudar durante o jogo.""" 
        self.ships_left = self.ai_settings.ship_limit
