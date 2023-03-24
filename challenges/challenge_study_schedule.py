def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for period in permanence_period:
            if target_time >= period[0] and target_time <= period[1]:
                count += 1
        ## Retorna para uma entrada específica a quantidade de estudantes presentes
        return count
    except Exception:
        ## None se permanence_period hourver alguma entrada inválida e se target_time recebe valor vazio
        None 
