    
    ENTER values for environment variables in .example.env file and then rename file to .env 
    
    
    
    You can filter tasks based on the status query parameter (e.g., /agendaList/?status=Pending).

    You can sort tasks based on the sort_by query parameter (e.g., /agendaList/?sort_by=due_date).

    You can search for tasks based on the search query parameter (e.g., /agendaList/?search=important).

    Pagination is implemented using the page and page_size query parameters (e.g., /agendaList/?page=2&page_size=20). It defaults to page 1 with a page size of 10.