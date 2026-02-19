/**
 * Hash Navigation Helper
 * Automatically opens <details> blocks (admonitions) when they or their
 * children are targeted by a URL hash.
 */
function handleHashNavigation() {
    const hash = window.location.hash;
    if (!hash) return;

    try {
        const target = document.querySelector(hash);
        if (!target) return;

        // Find all parent <details> elements
        let parent = target.closest('details');
        while (parent) {
            parent.setAttribute('open', 'open');
            parent = parent.parentElement.closest('details');
        }

        // Scroll to the target with a small offset for the sticky header
        setTimeout(() => {
            const headerOffset = 70;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }, 100);
    } catch (e) {
        console.warn("Hash navigation failed:", e);
    }
}

// Listen for hash changes and initial load
window.addEventListener('hashchange', handleHashNavigation);
document.addEventListener('DOMContentLoaded', handleHashNavigation);
// Also listen for MkDocs Material instant loading
if (typeof subscribe === 'function') {
    subscribe(handleHashNavigation);
}
