/**
 * Professional Telegram Admin Auth
 * Uses the official Telegram Login Widget to verify identity against hashed admin data.
 */

// Global callback for the Telegram Widget
window.onTelegramAuth = async function (user) {
    console.log("Telegram Auth callback triggered", user);

    const authData = await AdminAuth.fetchAdmins();
    const userHash = await AdminAuth.sha256(user.id.toString());

    console.log("User ID:", user.id);
    console.log("Calculated Hash:", userHash);
    console.log("Available Hashes:", authData);

    if (authData.includes(userHash)) {
        localStorage.setItem('is_admin_authorized', 'true');
        location.reload();
    } else {
        alert("Access Denied: Your Telegram ID (" + user.id + ") is not in the authorized list. Please ensure you have added this ID to the GitHub Secrets.");
    }
};

const AdminAuth = {
    async check() {
        const adminContent = document.getElementById('admin-content');
        const authGate = document.getElementById('auth-gate');
        if (!adminContent || !authGate) return;

        if (localStorage.getItem('is_admin_authorized') === 'true') {
            adminContent.style.display = 'block';
            authGate.style.display = 'none';
            return;
        }

        // Show official login gate
        authGate.style.display = 'block';
        adminContent.style.display = 'none';
    },

    async fetchAdmins() {
        try {
            // Priority 1: Relative to root (works for /administration/ on GitHub Pages)
            // Priority 2: Simple relative (works for local dev or different structures)
            const paths = ['/TCL-Discussion-Telegram/assets/admins.json', '/assets/admins.json', '../assets/admins.json'];

            for (const path of paths) {
                try {
                    const response = await fetch(path);
                    if (response.ok) return await response.json();
                } catch (e) { }
            }

            console.error("Could not find admins.json in any location.");
            return [];
        } catch (e) {
            console.error("Failed to load admin list", e);
            return [];
        }
    },

    async sha256(message) {
        try {
            const msgUint8 = new TextEncoder().encode(message);
            const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        } catch (e) {
            console.error("Hashing failed", e);
            return "";
        }
    }
};

document.addEventListener("DOMContentLoaded", () => AdminAuth.check());
