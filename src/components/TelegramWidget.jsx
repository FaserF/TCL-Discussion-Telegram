import React, { useEffect, useRef } from 'react';

const TelegramWidget = ({ post, width = '100%', discussion = false, dark = false }) => {
    const containerRef = useRef(null);

    useEffect(() => {
        // Clear previous widget if any
        if (containerRef.current) {
            containerRef.current.innerHTML = '';
        }

        const script = document.createElement('script');
        script.src = 'https://telegram.org/js/telegram-widget.js?22';
        script.async = true;
        script.setAttribute('data-telegram-post', post);
        script.setAttribute('data-width', width);
        script.setAttribute('data-userpic', 'true');

        if (dark) {
            script.setAttribute('data-dark', '1');
        }

        if (discussion) {
            script.setAttribute('data-comments-limit', '5');
            script.setAttribute('data-discussion', 'true');
        }

        containerRef.current.appendChild(script);
    }, [post, width, discussion, dark]);

    return (
        <div
            ref={containerRef}
            className="telegram-widget-container flex justify-center bg-black/5 dark:bg-white/5 rounded-2xl overflow-hidden min-h-[200px]"
        >
            {/* Widget will be injected here */}
        </div>
    );
};

export default TelegramWidget;
