def solve(candidate):
    if is_solution(candidate):
        process_solution(candidate)
        return
    for next_candidate in generate_candidates(candidate):
        if is_valid(next_candidate):
            solve(next_candidate)
            undo_move(next_candidate)