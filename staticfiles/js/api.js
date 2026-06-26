const TOKEN_KEY = "sgc_access_token";
const REFRESH_KEY = "sgc_refresh_token";

function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

function setTokens(data) {
    localStorage.setItem(TOKEN_KEY, data.access);
    localStorage.setItem(REFRESH_KEY, data.refresh);
}

function logout() {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(REFRESH_KEY);
    window.location.href = "/login/";
}

function requireAuth() {
    if (!getToken()) {
        window.location.href = "/login/";
    }
}

async function apiFetch(url, options = {}) {
    const headers = {
        "Content-Type": "application/json",
        ...options.headers,
    };

    const token = getToken();
    if (token) {
        headers.Authorization = `Bearer ${token}`;
    }

    const response = await fetch(url, {
        ...options,
        headers,
    });

    if (response.status === 401) {
        logout();
        return;
    }

    const text = await response.text();
    const data = text ? JSON.parse(text) : null;

    if (!response.ok) {
        const message = data?.detail || data?.erro || JSON.stringify(data);
        throw new Error(message || "Erro ao chamar a API");
    }

    return data;
}

function formatCurrency(value) {
    return Number(value).toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
    });
}
