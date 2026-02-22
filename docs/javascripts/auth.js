/**
 * Professional Telegram Admin Auth
 * Uses the official Telegram Login Widget to verify identity against hashed admin data.
 */
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

        // Official Telegram Callback
        window.onTelegramAuth = async (user) => {
            const authData = await this.fetchAdmins();
            const userHash = await this.sha256(user.id.toString());

            if (authData.includes(userHash)) {
                localStorage.setItem('is_admin_authorized', 'true');
                location.reload();
            } else {
                alert("Access Denied: You are not registered as an administrator.");
            }
        };
    },

    async fetchAdmins() {
        try {
            const response = await fetch('../assets/admins.json');
            return await response.json();
        } catch (e) {
            console.error("Failed to load admin list", e);
            return [];
        }
    },

    async sha256(message) {
        const msgUint8 = new TextEncoder().encode(message);
        const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }
};

document.addEventListener("DOMContentLoaded", () => AdminAuth.check());
