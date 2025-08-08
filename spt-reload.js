let count = 0;
const maxVisits = 500; // Adjust as needed
const url = 'https://open.spotify.com/genre/0JQ5DAqbMKFKDIyhfS9NTT?_reload_cause=mera-marzi-kya-kar-lega-re-tu';

function visitPage() {
  if (count < maxVisits) {
    count++;
    window.location.href = url; // Redirect to URL
  } else {
    console.log(`Visited ${count} times — stopping`);
  }
}

// Wait a second between reloads to avoid rapid loops
setTimeout(visitPage, 100);
