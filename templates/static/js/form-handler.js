document.querySelector("form").addEventListener("submit", function(event) {
    const params = new URLSearchParams();
    let hasValue = false; 

    Array.from(this.elements).forEach(input => {
        if (input.name && input.value) {
            params.append(input.name, input.value);
            hasValue = true;
        }
    });

    event.preventDefault();

    if (hasValue) window.location.href = `/?${params.toString()}`;
    else window.location.href = `/`;
});
