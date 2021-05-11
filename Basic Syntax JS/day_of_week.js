function calculateDayOfWeek(day) {
    let result;

    if (day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' 
                        || day == 'Friday' || day == 'Saturday' || day == 'Sunday'){
        switch (day) {
            case 'Monday': result = 1; break;
            case 'Tuesday': result = 2; break;
            case 'Wednesday': result = 3; break;
            case 'Thursday': result = 4; break;
            case 'Friday': result = 5; break; 
            case 'Saturday': result = 6; break;
            case 'Sunday': result = 7; break;
        } 
            console.log(result);
        } else {
            console.log('error');
        }
}

calculateDayOfWeek('Monday')