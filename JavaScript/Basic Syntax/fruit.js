function calculate(fruit, weightGrams, priceKilogram) {
    let weightKilogram = weightGrams / 1000
    let moneyNeeded = weightKilogram * priceKilogram

    console.log(`I need $${moneyNeeded.toFixed(2)} to buy ${weightKilogram.toFixed(2)} kilograms ${fruit}.`)
}

calculate('orange', 2500, 1.80)