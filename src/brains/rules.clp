(deftemplate  around 
    (multislot current)
    (multislot left) 
    (multislot right) 
    (multislot bottom) 
    (multislot top) 
    (multislot bottom-left) 
    (multislot bottom-right)
    (multislot top-left)
    (multislot top-right)
)

;positions row col element
;element untuk yang udah open dan 0 tetap 0
;element untuk yang belum terbuka nil

;mark row col notvisible
;notvisible bernilai 0 jika sudah dicek
;notvisible bernilai 1 jika belum dibuka

;markBomb row col isBomb
;isBomb bernilai 0 jika tidak bomb
;isBomb bernilai 1 jika bomb

(defrule topLeft
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row 0))
    (test (eq ?col 0))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left nil nil)
            (right ?row (+ ?col 1))
            (bottom (+ ?row 1) ?col)
            (top nil nil)
            (bottom-left nil nil)
            (bottom-right (+ ?row 1) (+ ?col 1))
            (top-left nil nil)
            (top-right nil nil)
        )
    )
)

(defrule top
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row 0))
    (test (neq ?col 0))
    (test (neq ?col (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right ?row (+ ?col 1))
            (bottom (+ ?row 1) ?col)
            (top (- ?row 1) ?col)
            (bottom-left (+ ?row 1) (- ?col 1))
            (bottom-right (+ ?row 1) (+ ?col 1))
            (top-left (- ?row 1) (- ?col 1))
            (top-right (- ?row 1) (+ ?col 1))
        )
    )
)

(defrule bottom
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row (- ?size 1)))
    (test (neq ?col 0))
    (test (neq ?col (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right ?row (+ ?col 1))
            (bottom (+ ?row 1) ?col)
            (top nil nil)
            (bottom-left (+ ?row 1) (- ?col 1))
            (bottom-right (+ ?row 1) (+ ?col 1))
            (top-left nil nil)
            (top-right nil nil)
        )
    )
)

(defrule left
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?col 0))
    (test (neq ?row 0))
    (test (neq ?row (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left nil nil)
            (right ?row (+ ?col 1))
            (bottom (+ ?row 1) ?col)
            (top (- ?row 1) ?col)
            (bottom-left nil nil)
            (bottom-right (+ ?row 1) (+ ?col 1))
            (top-left nil nil)
            (top-right (- ?row 1) (+ ?col 1))
        )
    )
)

(defrule right
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?col (- ?size 1)))
    (test (neq ?row 0))
    (test (neq ?row (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right nil nil)
            (bottom (+ ?row 1) ?col)
            (top (- ?row 1) ?col)
            (bottom-left (+ ?row 1) (- ?col 1))
            (bottom-right nil nil)
            (top-left (- ?row 1) (- ?col 1))
            (top-right nil nil)
        )
    )
)

(defrule topRight
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row 0))
    (test (eq ?col (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right nil nil)
            (bottom (+ ?row 1) ?col)
            (top nil nil)
            (bottom-left (+ ?row 1) (- ?col 1))
            (bottom-right nil nil)
            (top-left nil nil)
            (top-right nil nil)
        )
    )
)

(defrule bottomLeft
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row (- ?size 1)))
    (test (eq ?col 0))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left nil nil)
            (right ?row (+ ?col 1))
            (bottom nil nil)
            (top (- ?row 1) ?col)
            (bottom-left nil nil)
            (bottom-right nil nil)
            (top-left (- ?row 1) (- ?col 1))
            (top-right (- ?row 1) (+ ?col 1))
        )
    )
)

(defrule bottomRight
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (eq ?row (- ?size 1)))
    (test (eq ?col (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right nil nil)
            (bottom nil nil)
            (top (- ?row 1) ?col)
            (bottom-left nil nil)
            (bottom-right nil nil)
            (top-left (- ?row 1) (- ?col 1))
            (top-right nil nil)
        )
    )
)

(defrule middle
    (positions ?row ?col ?element)
    (board_size ?size)
    (test (neq ?row 0))
    (test (neq ?col 0))
    (test (neq ?row (- ?size 1)))
    (test (neq ?col (- ?size 1)))
=>
    (assert
        (around
            (current ?row ?col ?element)
            (left ?row (- ?col 1))
            (right ?row (+ ?col 1))
            (bottom (+ ?row 1) ?col)
            (top (- ?row 1) ?col)
            (bottom-left (+ ?row 1) (- ?col 1))
            (bottom-right (+ ?row 1) (+ ?col 1))
            (top-left (- ?row 1) (- ?col 1))
            (top-right (- ?row 1) (+ ?col 1))
        )
    )
)

(defrule isBomb
    (around (current ?row ?col ?element) 
            (left ?left_row ?left_col) 
            (right ?right_row ?right_col) 
            (bottom ?bot_row ?bot_col) 
            (top ?top_row ?top_col) 
            (bottom-left ?bot_left_row ?bot_left_col) 
            (bottom-right ?bot_right_row ?bot_right_col) 
            (top-left ?top_left_row ?top_left_col) 
            (top-right ?top_right_row ?top_right_col)
    )
    (mark ?left_row ?left_col ?mark_left)
    (mark ?right_row ?right_col ?mark_right)
    (mark ?bot_row ?bot_col ?mark_bot)
    (mark ?top_row ?top_col ?mark_top)
    (mark ?bot_left_row ?bot_left_col ?mark_bot_left)
    (mark ?bot_right_row ?bot_right_col ?mark_bot_right)
    (mark ?top_left_row ?top_left_col ?mark_top_left)
    (mark ?top_right_row ?top_right_col ?mark_top_right)
    (test (eq (+ ?mark_left ?mark_right ?mark_bot ?mark_top ?mark_bot_left ?mark_bot_right ?mark_top_left ?mark_top_right) ?element))
=>  
    (assert (bomb ?left_row ?left_col ?mark_left))
    (assert (bomb ?right_row ?right_col ?mark_right))
    (assert (bomb ?bot_row ?bot_col ?mark_bot))
    (assert (bomb ?top_row ?top_col ?mark_top))
    (assert (bomb ?bot_left_row ?bot_left_col ?mark_bot_left))
    (assert (bomb ?bot_right_row ?bot_right_col ?mark_bot_right))
    (assert (bomb ?top_left_row ?top_left_col ?mark_top_left))
    (assert (bomb ?top_right_row ?top_right_col ?mark_top_right))

    (assert (markBomb ?left_row ?left_col ?mark_left))
    (assert (markBomb ?right_row ?right_col ?mark_right))
    (assert (markBomb ?bot_row ?bot_col ?mark_bot))
    (assert (markBomb ?top_row ?top_col ?mark_top))
    (assert (markBomb ?bot_left_row ?bot_left_col ?mark_bot_left))
    (assert (markBomb ?bot_right_row ?bot_right_col ?mark_bot_right))
    (assert (markBomb ?top_left_row ?top_left_col ?mark_top_left))
    (assert (markBomb ?top_right_row ?top_right_col ?mark_top_right))
)

(defrule delNotBomb
    (bomb ?row ?col 0)
    (test (neq ?row nil))
    (test (neq ?col nil))
    ?f1 <- (bomb ?row ?col 0)
=>
    (retract ?f1)
)

(defrule chooseTiles
    (around (current ?row ?col ?element) 
            (left ?left_row ?left_col) 
            (right ?right_row ?right_col) 
            (bottom ?bot_row ?bot_col) 
            (top ?top_row ?top_col) 
            (bottom-left ?bot_left_row ?bot_left_col) 
            (bottom-right ?bot_right_row ?bot_right_col) 
            (top-left ?top_left_row ?top_left_col) 
            (top-right ?top_right_row ?top_right_col)
    )
    (markBomb ?left_row ?left_col ?bomb_left)
    (markBomb ?right_row ?right_col ?bomb_right)
    (markBomb ?bot_row ?bot_col ?bomb_bot)
    (markBomb ?top_row ?top_col ?bomb_top)
    (markBomb ?bot_left_row ?bot_left_col ?bomb_bot_left)
    (markBomb ?bot_right_row ?bot_right_col ?bomb_bot_right)
    (markBomb ?top_left_row ?top_left_col ?bomb_top_left)
    (markBomb ?top_right_row ?top_right_col ?bomb_top_right)
    (test (eq (+ ?bomb_left ?bomb_right ?bomb_bot ?bomb_top ?bomb_bot_left ?bomb_bot_right ?bomb_top_left ?bomb_top_right) ?element))
=>
    (assert (tiles ?left_row ?left_col ?bomb_left))
    (assert (tiles ?right_row ?right_col ?bomb_right))
    (assert (tiles ?bot_row ?bot_col ?bomb_bot))
    (assert (tiles ?top_row ?top_col ?bomb_top))
    (assert (tiles ?bot_left_row ?bot_left_col ?bomb_bot_left))
    (assert (tiles ?bot_right_row ?bot_right_col ?bomb_bot_right))
    (assert (tiles ?top_left_row ?top_left_col ?bomb_top_left))
    (assert (tiles ?top_right_row ?top_right_col ?bomb_top_right))
)

(defrule delTilesInBombs
    ?f1 <- (tiles ?row ?col 1)
=>
    (retract ?f1)
)

(defrule delTilesInPosition
    (positions ?row ?col ?mark)
    (test (neq ?mark nil))
    ?f1 <- (tiles ?row ?col ?element)
=>
    (retract ?f1)
)