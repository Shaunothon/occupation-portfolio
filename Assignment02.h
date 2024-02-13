#include <iostream>
#include <vector>
#include <iomanip>

class knightType
{
public:
struct position
{
    position(int r = 0, int c = 0, int o = 0)
    {
        row = r;
        col = c;
        onwardMoves = o;
    }
    int row;
    int col;
    int onwardMoves;
};
knightType(int = 8);
bool knightTour(int , int);
void outputTour () const;
private:
bool knightTour(int , int , int);
std::vector <position > getAvailableMoves(int , int);
bool fullBoard ();
std::vector < std::vector <int > > board;
int functionsCalled;
};
///@brief default constructor
///
///@param dim dimension amount for row and column chessboard
knightType::knightType(int dim){
    std::vector<int> temp (8,0);
    board.resize(dim, temp);
    functionsCalled = 0;
}

///@brief KnightTour public
///
///@param r row
///@param c column
///
///@return KnightTour private true or false value
bool knightType::knightTour(int r, int c ){
    return knightTour(r, c, 1);
}

///@brief OutputTour Outputs chess moves
///
void knightType::outputTour() const{
std::cout << "   ";
for(char alpha = 'A'; alpha <  static_cast<char>('A' + board.size()); alpha++){
    std::cout << std::setw(3) << alpha;
}
std::cout << '\n';

for( char alpha = 'A'; alpha <  static_cast<char>('A' + board.size()); alpha++){
    std::cout << std::setw(3) << alpha;
    for(unsigned long i = 0; i < board.size(); i++){
        std::cout << std::setw(3) << board[alpha - 'A'][i];
    }
    std::cout << std::endl;

}
std::cout << "\nFunctions called: " << functionsCalled << '\n';
}

///@brief knightTour private finds least amount of onward moves
///to complete the board
///
///@param r row
///@param c column
///@param tourIndex index of knight chess piece
///
///@return true if board is full, else, returns false.
bool knightType::knightTour(int r, int c, int tourIndex){
    board[r][c] = tourIndex;
    functionsCalled++;

    if(fullBoard()){

        return true;
    }

    std::vector<knightType::position> newVec = getAvailableMoves(r, c);
    while(!newVec.empty()){

        auto last  = newVec.end();
        auto min   = newVec.begin();
        auto next  = min + 1;

        while(next != last){
            if(min->onwardMoves > next->onwardMoves){

                min = next;
                next++;
            }
            else{
                next++;
            }
        }
            if(knightTour(min->row, min->col, tourIndex + 1) == true){
                return true;
            }
            else{
                newVec.erase(min);
            }
    }
    return false;
}
///@brief getAvailableMoves calculates next available moves for coordinate
///
///@param r row
///@param c column
///
///@return vector with available moves
std::vector<knightType::position> knightType::getAvailableMoves(int r, int c){

    std::vector<position> knightMoves;

    int rowOffset[8]= {-2, -2, -1, -1, 1, 1, 2, 2};
    int colOffset[8]= {-1, 1, -2, 2, -2, 2, -1, 1};
// find all possible moves
    for(int i = 0; i < 8; i++){
        unsigned long calcRow = rowOffset[i] + r;
        unsigned long calcCol = colOffset[i] + c;
// check validity of moves (out of range)
        if (calcRow >= 0 && calcRow < board.size() &&
            calcCol >= 0 && calcCol < board.size() &&
            board[calcRow][calcCol] == 0){
            knightMoves.push_back(position(0, 0, 0));
            auto size = knightMoves.size() - 1;
            knightMoves[size].row = rowOffset[i]+ r;
            knightMoves[size].col = colOffset[i] + c;
// check possible moves from subsequent move
            for(int j = 0; j < 8; j++){
                unsigned long newR = knightMoves[size].row + rowOffset[j];
                unsigned long newC = knightMoves[size].col + colOffset[j];

// counts move towards total if in range
                if (newR >= 0 && newR < board.size() &&
                    newC >= 0 && newC < board.size() &&
                    board[newR][newC] == 0 && !
                    (static_cast<unsigned long>(r) == newR &&
                    static_cast<unsigned long>(c)== newC)){

                        knightMoves[size].onwardMoves++;
                }

            }

        }
    }
    return knightMoves;
}

///@brief fullboard
///
///@return true if board is full, false otherwise.
bool knightType::fullBoard(){
    bool is_full = true;
    for(unsigned long i = 0; i < board.size(); i++){
        for(unsigned long j = 0; j < board.size(); j++){
            if(board[i][j] == 0){
                is_full = false;
            }
        }
    }
    return is_full;
}


