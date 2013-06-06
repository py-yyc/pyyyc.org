<h1>Upcoming Events</h1>
{{^upcomingEvents}}
Unfortunately, there are no events coming up. Stay tuned for more!
{{/upcomingEvents}}
{{#upcomingEvents}}
{{> eventTpl}}
{{/upcomingEvents}}

<h1>Past Events</h1>
{{#pastEvents}}
{{> eventTpl}}
{{/pastEvents}}