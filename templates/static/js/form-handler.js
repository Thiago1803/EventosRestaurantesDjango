document.querySelector("form").addEventListener("submit", function(event) {
    const params = new URLSearchParams();
    let hasValue = false; 

    Array.from(this.elements).forEach(input => {
        if (input.name && input.value) {
            params.append(input.name, input.value);
            hasValue = true;
        }
    });

    if (!hasValue) {
        event.preventDefault();
        return;
    }

    event.preventDefault();
    window.location.href = `?${params.toString()}`;
});
