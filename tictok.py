       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
    
def is_draw():
    if "  " not in board:
        return True
    else:
        return False

cat /var/log/nginx/access.log|awk 'BEGIN { print "url", "status code" } { print $8 " "  $9 |"sort" }'|grep 502

p = subprocess.Popen(" cat /var/log/nginx/access.log|awk 'BEGIN { print "url", "status code" } { print $8 " "  $9 |"sort" }'|grep 502", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]




while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break

    \\
He is very good at handling Linux systems and keeping the environment up to date and Strong debugging skills , also he has handes on experience with DevOps space and good contributer in automation.



proc = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 502", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
(out, err) = proc.communicate()
print "program output:", out


