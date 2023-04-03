import statsmodels.formula.api as smf


def create_and_train_model(dataset, ankle):
    # formula for this model
    formula = "Neck ~ Ankle"

    # create a model
    model = smf.ols(formula=formula, data=dataset)

    # train a model
    fitted_model = model.fit()

    # show parameters
    ans = input("Would you like to see a parameters? [y/n]\n")
    if ans.lower() == "y":
        print(f"Model parameters\nLine slope:{fitted_model.params[1]}\nLine Interrupt:{fitted_model.params[0]}")

    approximate_neck = fitted_model.predict(ankle)

    return approximate_neck
