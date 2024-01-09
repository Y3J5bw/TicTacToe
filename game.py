from itertools import combinations


class Board:
    def __init__(self):
        self.tileList = [[True, None] for _ in range(9)]
        self.winningCombinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


    def tileCheck(self, userInput):
        if self.tileList[userInput][0] is True:
            self.tileList[userInput][0] = False
            return True
        return False


    def boardCheck(self):
        playerOneTiles, playerTwoTiles = ([(index) for index, state in enumerate(self.tileList) if False in state and player in state] for player in ('X', 'O'))
        playerOneTilesCombinations, playerTwoTilesCombinations = (list(combinations(player, 3)) for player in (playerOneTiles, playerTwoTiles))
        for comboLists in (playerOneTilesCombinations, playerTwoTilesCombinations):
            for combo in comboLists:
                if combo in self.winningCombinations and combo in playerOneTilesCombinations:
                    return 'p1 wins'
                elif combo in self.winningCombinations and combo in playerTwoTilesCombinations:
                    return 'p2 wins'
        if sum(state.count(True) for state in self.tileList) == 0:
            return 'tie'
        return 'continue'


    def tileListUpdate(self, tile, player, clear=False):
        if clear is False:
            self.tileList[tile][1] = player
        else:
            self.tileList = [[True, None] for _ in range(9)]


class Player:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.currentPlayer = self.players[0]

    def playerCheck(self):
        if self.currentPlayer == self.players[0]:
            return 'X'
        return 'O'

    def playerTurnChange(self, player):
        if player == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]


if __name__ == '__main__':
    b = Board()
    p = Player('X', 'O')