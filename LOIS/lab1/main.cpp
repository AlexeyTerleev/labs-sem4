#include "iostream"
#include "vector"
#include "algorithm"


std::vector<std::string> get_duplicate_variables(const std::string& formula) {
    std::vector<std::string> variables;
    std::string curr_var;

    std::string operators = "!+*()";
    for (char sign: formula) {
        if (operators.find(sign) != std::string::npos && !curr_var.empty()) {

            variables.push_back(curr_var);

            curr_var.clear();
        }
        else if (operators.find(sign) == std::string::npos) {
            curr_var.push_back(sign);
        }
    }
    if (!curr_var.empty()) {
        variables.push_back(curr_var);
    }
    return variables;
}

std::vector<std::string> get_set(const std::vector<std::string>& variables) {
    std::vector<std::string> set;
    for (const std::string& var: variables){
        if (std::find(set.begin(), set.end(), var) == set.end())
            set.push_back(var);
    }
    return set;
}

std::vector<std::string> get_variables(const std::string& formula) {
    return get_set(get_duplicate_variables(formula));
}

std::vector<std::string> get_sub_formulas(const std::string& formula) {
    std::vector<std::string> sub_formulas;
    std::string curr_sub_formula;
    bool opened = false;
    for(char sign: formula) {
        if (sign == '(') {
            opened = true;
        }
        else if (sign == ')') {
            opened = false;

            sub_formulas.push_back(curr_sub_formula);
            curr_sub_formula.clear();
        }
        else if (opened) {
            curr_sub_formula.push_back(sign);
        }
    }
    return sub_formulas;
}


bool spaces_check(const std::string& formula) {
    return formula.find(' ') == std::string::npos;
}

bool sign_check(const std::string& formula) {
    std::string operators = "!+*()";
    for (char sign: formula) {
        if (operators.find(sign) == std::string::npos &&
            (sign < 48 || sign > 57) && (sign < 65 || sign > 90) && (sign < 97 || sign > 122))
            return false;
    }
    return true;
}

bool brackets_check(const std::string& formula) {

    bool opened = false, closed = true;
    for(char sign: formula) {
        if (sign == '(') {
            if (opened || !closed) {
                return false;
            }
            opened = true;
            closed = false;
        }
        else if (sign == ')') {
            if (!opened || closed) {
                return false;
            }
            opened = false;
            closed = true;
        }
    }

    if(formula.at(0) != '(' || formula.at(formula.length() - 1) != ')')
        return false;

    return true;
}

bool negation_check(const std::string& formula) {
    std::string operators = "+*()";

    for(int i = 0; i < formula.length() - 1; i++) {
        if (formula.at(i) == '!' && operators.find(formula[i + 1]) != std::string::npos) {
            return false;
        }
    }

    return true;
}

bool disjunction_check (const std::string& formula) {
    bool opened = false;
    for(char sign: formula) {
        if (sign == '(') {
            opened = true;
        }
        else if (sign == ')') {
            opened = false;
        }
        else if (sign == '+' && opened) {
            return false;
        }
    }
    return true;
}

bool conjunction_check (const std::string& formula) {

    for(std::string sub_formula: get_sub_formulas(formula)) {
        if (sub_formula.at(0) == '*' || sub_formula.at(sub_formula.length() - 1) == '*')
            return false;
    }

    bool opened = false;
    for(char sign: formula) {
        if (sign == '(') {
            opened = true;
        }
        else if (sign == ')') {
            opened = false;
        }
        else if (sign == '*' && !opened) {
            return false;
        }
    }

    return true;
}

bool variables_check (const std::string& formula) {

    bool opened = false;
    for(char sign: formula) {
        if (sign == '(') {
            opened = true;
        }
        else if (sign == ')') {
            opened = false;
        }
        else if (sign != '+' && !opened) {
            return false;
        }
    }

    auto variables = get_variables(formula);
    std::sort(variables.begin(), variables.end());

    for(std::string& sub_formula: get_sub_formulas(formula)) {
        auto sub_formula_variables = get_duplicate_variables(sub_formula);
        std::sort(sub_formula_variables.begin(), sub_formula_variables.end());

        if (variables != sub_formula_variables) {
            return false;
        }
    }

    return true;
}


int main() {
    std::string formula;

    std::cout << "Enter formula: "; std::getline(std::cin, formula);

    if (formula.empty()) {
        std::cout << "Please, enter formula";
        return 0;
    }
    if (!spaces_check(formula)) {
        std::cout << "Please, enter formula without spaces";
        return 0;
    }
    if (!sign_check(formula)) {
        std::cout << "The formula must consist only of symbols +, *, !, (, ), "
                     "numbers, uppercase and lowercase English letters!";
        return 0;
    }
    if (!brackets_check(formula)) {
        std::cout << "Please, check the placement of brackets";
        return 0;
    }
    if(!negation_check(formula)) {
        std::cout << "Please, check the placement of negation, ! can only appear before a variable";
        return 0;
    }
    if(!disjunction_check(formula)) {
        std::cout << "Please, check the placement of disjunction";
        return 0;
    }
    if(!conjunction_check(formula)) {
        std::cout << "Please, check the placement of conjunction";
        return 0;
    }
    if(!variables_check(formula)) {
        std::cout << "Please, check the placement of variables";
        return 0;
    }

    std::cout << "The formula is a perfect disjunctive normal form";

    return 0;
}
