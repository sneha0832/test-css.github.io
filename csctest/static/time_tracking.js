// TIME TRACKKING CODE
// THIS IS PUT INTO THE TEMPLATE PAGE

document.addEventListener("DOMContentLoaded", function() {
    var startTime = Date.now();
    
    function sendTimeSpent() {
        var endTime = Date.now();
        var timeSpent = endTime - startTime;

        fetch('/record_time_spent/', { // Make sure the path matches your Django URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Ensure CSRF token is sent with request
            },
            body: JSON.stringify({
                url: window.location.pathname,
                time_spent: timeSpent
            })
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    window.addEventListener("beforeunload", sendTimeSpent);
});
