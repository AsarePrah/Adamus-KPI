// dom.js
// Helpers for creating UI elements dynamically

const DOM = {
    createInputGroup: (labelText, id, type = 'text', placeholder = '') => {
        const div = document.createElement('div');
        div.className = 'input-group';
        div.style.marginBottom = '10px';
        
        const label = document.createElement('label');
        label.className = 'small';
        label.textContent = labelText;
        label.style.display = 'block';
        label.style.marginBottom = '4px';
        label.style.fontSize = '12px';
        label.style.color = '#6b7280';
        
        const input = document.createElement('input');
        input.id = id;
        input.type = type;
        input.placeholder = placeholder || labelText;
        input.className = 'form-input';
        
        input.style.width = '100%';
        input.style.padding = '8px';
        input.style.border = '1px solid #d1d5db';
        input.style.borderRadius = '6px';
        input.style.boxSizing = 'border-box';

        label.appendChild(input);
        div.appendChild(label);
        return { container: div, input: input };
    },

    createButton: (text, onClick, variant = 'primary') => {
        const btn = document.createElement('button');
        btn.textContent = text;
        btn.className = 'btn';
        if (variant === 'ghost') {
            btn.style.backgroundColor = 'transparent';
            btn.style.color = 'var(--text-primary)';
            btn.style.border = '1px solid #d1d5db';
        }
        btn.addEventListener('click', onClick);
        return btn;
    },

    clear: (elementId) => {
        const el = document.getElementById(elementId);
        if (el) el.innerHTML = '';
    },

    showToast: (message, type = 'success') => {
        let toast = document.getElementById('toast-msg');
        if (toast) toast.remove();
        
        toast = document.createElement('div');
        toast.id = 'toast-msg';
        toast.textContent = message;
        toast.style.position = 'fixed';
        toast.style.bottom = '20px';
        toast.style.right = '20px';
        toast.style.padding = '12px 24px';
        toast.style.borderRadius = '8px';
        toast.style.color = '#fff';
        toast.style.backgroundColor = type === 'success' ? '#10b981' : '#ef4444';
        toast.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
        toast.style.zIndex = '1000';
        
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 3000);
    }
};
