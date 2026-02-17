import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { MessageSquare, Menu, X, Monitor, Search as SearchIcon, Command, Sun, Moon } from 'lucide-react';
import { Link, useLocation } from 'react-router-dom';
import Search from './Search';

const Navbar = ({ theme, toggleTheme }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [isSearchOpen, setIsSearchOpen] = useState(false);
    const [scrolled, setScrolled] = useState(false);
    const location = useLocation();

    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20);
        const handleKeyDown = (e) => {
            if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
                e.preventDefault();
                setIsSearchOpen(true);
            }
        };

        window.addEventListener('scroll', handleScroll);
        window.addEventListener('keydown', handleKeyDown);
        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('keydown', handleKeyDown);
        };
    }, []);

    const navLinks = [
        { name: 'Home', path: '/' },
        { name: 'Encyclopedia', path: '/guides' },
        { name: 'FAQ', path: '/faq' },
        { name: 'Contribute', path: '/contribute' },
    ];

    return (
        <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'py-4' : 'py-6'
            }`}>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className={`glass rounded-2xl px-6 transition-all duration-300 ${scrolled ? 'border-tcl-red/20 dark:border-tcl-red/20 border-opacity-100 bg-white/80 dark:bg-black/80' : 'border-transparent bg-transparent'
                    }`}>
                    <div className="flex items-center justify-between h-16">
                        <Link to="/" className="flex items-center gap-3 group">
                            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-tcl-red to-tcl-accent flex items-center justify-center glow group-hover:-rotate-12 transition-transform shadow-lg">
                                <Monitor className="text-white w-6 h-6" />
                            </div>
                            <div className="flex flex-col">
                                <span className="text-gray-900 dark:text-white font-black text-xl leading-none">Community <span className="text-tcl-red italic">Resource</span></span>
                                <span className="text-[10px] text-gray-500 font-bold uppercase tracking-widest mt-0.5">TCL Firmware Discussion</span>
                            </div>
                        </Link>

                        {/* Desktop Nav */}
                        <div className="hidden md:flex items-center gap-1">
                            <button
                                onClick={() => setIsSearchOpen(true)}
                                className="flex items-center gap-6 px-4 py-2 rounded-xl text-sm font-medium text-gray-500 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5 transition-all mr-4 border border-transparent hover:border-black/5 dark:hover:border-white/10"
                            >
                                <div className="flex items-center gap-2">
                                    <SearchIcon size={16} />
                                    <span>Quick Search...</span>
                                </div>
                                <div className="flex items-center gap-1 px-1.5 py-0.5 rounded bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/10 text-[10px] font-bold">
                                    <Command size={10} /> K
                                </div>
                            </button>

                            {navLinks.map((link) => (
                                <Link
                                    key={link.name}
                                    to={link.path}
                                    className={`px-5 py-2 rounded-xl text-sm font-bold tracking-tight transition-all hover:bg-black/5 dark:hover:bg-white/5 ${location.pathname === link.path ? 'text-tcl-red' : 'text-gray-500 dark:text-gray-400'
                                        }`}
                                >
                                    {link.name}
                                </Link>
                            ))}
                            <div className="w-px h-6 bg-black/10 dark:bg-white/10 mx-4" />

                            <button
                                onClick={toggleTheme}
                                className="p-2.5 rounded-xl text-gray-500 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5 transition-all mr-2 border border-transparent hover:border-black/5 dark:hover:border-white/10"
                                title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`}
                            >
                                {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
                            </button>

                            <a
                                href="https://t.me/tclupdates_discussion"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="px-6 py-2.5 rounded-xl bg-tcl-red text-white text-sm font-black hover:scale-105 active:scale-95 transition-all shadow-lg glow flex items-center gap-2"
                            >
                                <MessageSquare className="w-4 h-4" />
                                <span>Join Group</span>
                            </a>
                        </div>

                        {/* Mobile Button */}
                        <div className="md:hidden flex items-center gap-2">
                            <button
                                onClick={() => setIsSearchOpen(true)}
                                className="p-2 rounded-xl glass border-white/5 text-gray-400 hover:text-white transition-colors"
                            >
                                <SearchIcon className="w-6 h-6" />
                            </button>
                            <button
                                onClick={() => setIsOpen(!isOpen)}
                                className="p-2 rounded-xl glass border-white/5 text-gray-400 hover:text-white transition-colors"
                            >
                                {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            {/* Mobile Drawer */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0.95 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.95 }}
                        className="fixed inset-0 top-[100px] z-40 p-4 md:hidden"
                    >
                        <div className="glass p-8 rounded-[2rem] border-white/10 shadow-2xl flex flex-col gap-6">
                            {navLinks.map((link) => (
                                <Link
                                    key={link.name}
                                    to={link.path}
                                    onClick={() => setIsOpen(false)}
                                    className={`text-2xl font-black ${location.pathname === link.path ? 'text-tcl-red' : 'text-white'
                                        }`}
                                >
                                    {link.name}
                                </Link>
                            ))}
                            <div className="h-px bg-white/5 w-full my-2" />
                            <a
                                href="https://t.me/tclupdates_discussion"
                                className="w-full py-5 rounded-2xl bg-tcl-red text-white text-center font-black text-xl shadow-lg"
                            >
                                Support Group
                            </a>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Search Modal */}
            <Search isOpen={isSearchOpen} onClose={() => setIsSearchOpen(false)} />
        </nav>
    );
};

export default Navbar;
