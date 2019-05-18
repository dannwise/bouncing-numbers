import time

def bouncing(desired_percentage):
    
    start_time = time.time()
    bouncing_numbers = []
    number = 0 
    percentage = 0
    
    """
    CHECKS INPUTS AND RAISES ASSERTION ERRORS IF CONDITIONS ARE NOT MET.
    """
    assert(type(desired_percentage) == float), 'The inputed value is not a float type value.'
    assert(desired_percentage > 0 and desired_percentage < 1), 'The desired percentage must be a float higher than 0 and lesser than 1'


    """
    LOOPS THROUGH NUMBERS APPENDING THE BOUNCING ONES TO A LIST AND USES IT'S LENGHT TO CALCULATE PERCENTAGE
    """
    while percentage < desired_percentage:
        last_percentage = percentage
        if ''.join(sorted(str(number))) == str(number) or ''.join(sorted(str(number), reverse=True)) == str(number):
            pass
        else:
            bouncing_numbers.append(number)
            percentage = len(bouncing_numbers)/number

        number += 1
        
    """
    TREAT THE CASE OF DESIRED PERCENTAGE BEING UNACHIEVABLE
    """
    if percentage > desired_percentage:
        return('The desired percentage cannot be achieved.', 
               'Lower closest percentage is: {}%, for which the least bouncing number is: {}.'.format(last_percentage*100, bouncing_numbers[-2]),
               'Higher closest percentage is: {}%, for which the least bouncing number is: {}.'.format(percentage*100, bouncing_numbers[-1]),
               'The results were found in {} seconds'.format(time.time() - start_time))


    return('The least bouncing number for the desired percentage of {}% is: {}, found in: {} seconds.'.format(percentage*100, 
                                                                                                              bouncing_numbers[-1],                                                                                                        
                                                                                                              time.time() - start_time))
