#include <iostream>

using namespace std;

int main() {
    // Sales Tax
    double sales = 95000;
    cout << "Sales: $" << sales << endl;
    // State Tax

    const double stateTaxRate = .04;
    double stateTax = sales * .04;
    cout << "State Tax: $" << stateTax << endl;

    const double countyTaxRate = .02;
    double countyTax = sales * countyTaxRate;
    cout << "County Tax: $" << countyTax << endl;

    double totalTax = stateTax + countyTax;
    cout << "Total Tax: $" << totalTax;
    
    return 0;
}