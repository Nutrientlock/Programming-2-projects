//Author: Ajay Clarke 
// Date: N/A 
// Description: Group Project (Add Employee)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Open File 
FILE *open_file();

// Close File
void close_file(FILE *file);

// function to appeand of create a new file
void Clean_file();

// Function to add Employee
void Add_Employee();

// Validate the uniqueness of ID number
int valid_id (char * idPtr);

// validate employee status
int Valid_status(char *status); 

// list Employees
void list_emplyees();

// Find Employee
void find_employee();

//Update Record
void Update_Record();



// struct to receive Employee data
typedef struct{
    char Employee_ID [10];
    char First_name [40];
    char Last_name [40];
    char Role [40];
    char Status [40];
} employee;

int main(){
    FILE *file = open_file();
    if (file == NULL) return 1;
    list_emplyees();
    close_file(file);
    find_employee();

    return 0;
}

FILE *open_file(){
    FILE *file;
    file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "a");
    if (file == NULL){
        printf("File failed to open");
        return NULL;
    }

    else {
        printf ("file open successful\n");
        Clean_file();
        return file;
    }

}

void close_file(FILE* file){
     fclose(file);

}

// function to appeand of create a new file
void Clean_file(){
    int clean_file;

    printf("Do you want a clean Document 1 for no and 0 for yes: ");
    scanf("%d", &clean_file);

    if (clean_file == 0){
        FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "w"); 
        fclose(file);
        Add_Employee();
    }
    else if (clean_file == 1){
        Add_Employee();
    }
    else {
        printf("Invalid Input");
    }

}

// Validate the uniqueness of ID number
int valid_id(char *idPtr) {
    char existingID[10];
    char line[200];

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    if (file == NULL) {
        return 0; 
    }

    while (fgets(line, sizeof(line), file) != NULL) {
       
        sscanf(line, "%[^,]", existingID); 

        if (strcmp(existingID, idPtr) == 0) {
            fclose(file);
            return 1; 
        }
    }

    fclose(file);
    return 0;
}

// validate employee status
int Valid_status(char *Status){
    int i = 0;
    while (Status[i] != '\0'){
        Status [i] = toupper(Status[i]);
        i += 1;
    }
    if (strcmp(Status, "ACTIVE") == 0){
        return 1;    
        }
    else
        if (strcmp(Status, "LEAVE") == 0){
        return 1;
        }
    else
        if (strcmp(Status, "TERMINATED") == 0){
        return 1;
        }
    else{
        printf("Invalid Input");
        return 0;
    }

}

// Function to add Employee
void Add_Employee() {
    employee emp;
    int starter = 0;
    char *idPtr = NULL;
    int validate ;

    do {
        printf("Press 1 Add Employee or -999 to stop: ");
        scanf("%d", &starter);
        if (starter > 1 || starter <= 0){
            break;
        }
        printf("Enter Employee ID,\nmust be 10 characters: ");
        scanf("%s", emp.Employee_ID);
        idPtr= emp.Employee_ID; 

        if (strlen(emp.Employee_ID) <= 10){

            if (valid_id(emp.Employee_ID) == 1) { 
                printf("Error: ID already exists. Try a different ID.\n");
                continue; 
            }

            printf("Enter Employee First name: ");
            scanf("%s", emp.First_name);

            printf("Enter Employee Last name: ");
            scanf("%s", emp.Last_name);

            printf("Enter Employee Role: ");
            scanf("%s", emp.Role);

            do {
            printf("Enter Employee, Status Active, on leave, or terminated: ");
            scanf("%s", emp.Status);
            
                if (Valid_status(emp.Status) == 0){
                    printf("\nError: Invalid Status. Must be Active, On Leave, or Terminated: \n");
                
                }
            }
            while(Valid_status(emp.Status) == 0);

            FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "a"); 

            if (file == NULL) {
                printf("File Failed to open\n");
                return; 
            }

            fprintf(file, "%s,%s,%s,%s,%s\n",  
                emp.Employee_ID,
                emp.First_name,
                emp.Last_name,
                emp.Role,
                emp.Status
            );

            fclose(file);
            printf("Employee added successfully.\n");

        }
        else {
            printf("ID Number is Invalid");
        }
    } while(starter != -999 || starter < 2);

}


void list_emplyees(){
    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");

    if (file == NULL) {
        printf("Error: Employee file not found.\n");
        return;
    }

    fseek(file, 0, SEEK_END);
    long int size = ftell(file);

    if (size == 0) {
        printf("No employees found. File is empty.\n");
        fclose(file);
        return;
    }

    rewind(file);

    char Employee_ID[10];
    char First_name[40];
    char Last_name[40];
    char Role[40];
    char Status[40];
    char line[200];

    // print table header
    printf("\n%-10s %-20s %-20s %-15s\n",
        "ID", "Full Name", "Role", "Status");
    printf("--------------------------------------------------------------\n");

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^\n]",
            Employee_ID,
            First_name,
            Last_name,
            Role,
            Status);

        // combine first and last name
        char Full_name[80];
        snprintf(Full_name, sizeof(Full_name), "%s %s", First_name, Last_name);

        printf("%-10s %-20s %-20s %-15s\n",
            Employee_ID,
            Full_name,
            Role,
            Status);
    }

    printf("--------------------------------------------------------------\n");
    fclose(file);
}


// find_employee
void find_employee(){

    char line [200];
    char ID_search [10];
    char ID_in_system[10];
    char Employee_ID[10];
    char First_name[40];
    char Last_name[40];
    char Role[40];
    char Status[40];
    
    

    printf("Enter the ID number of the person you wish to find: ");
    scanf("%s",ID_search);

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    
    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", ID_in_system); 
        if (strcmp(ID_in_system, ID_search) == 0 ){

            printf("\n%-10s %-20s %-20s %-15s\n", "ID", "Full Name", "Role", "Status");
            printf("--------------------------------------------------------------\n");
                sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^\n]",
                    Employee_ID,
                    First_name,
                    Last_name,
                    Role,
                    Status);

                // combine first and last name
                char Full_name[80];
                snprintf(Full_name, sizeof(Full_name), "%s %s", First_name, Last_name);

                printf("%-10s %-20s %-20s %-15s\n",
                    Employee_ID,
                    Full_name,
                    Role,
                    Status);
            
            printf("--------------------------------------------------------------\n");
            fclose(file);


        }

    }


}
// Update Record
void Update_Record(){
    char line [200];
    char ID_search [10];
    char ID_in_system[10];
    char Employee_ID[10];
    char First_name[40];
    char Last_name[40];
    char Role[40];
    char Status[40];
    
    printf("Enter the ID number of the record you wish to update: ");
    scanf("%s",ID_search);

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    
    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", ID_in_system); 
        if (strcmp(ID_in_system, ID_search) == 0 ){
            
        }
    }

}
