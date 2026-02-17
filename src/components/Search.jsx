import React, { useState, useEffect, useRef, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search as SearchIcon, X, ArrowRight, CornerDownLeft, Command, FileText, Cpu, AlertTriangle, MessageCircle } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { searchData } from '../data/searchData';

const Search = ({ isOpen, onClose }) => {
    const [query, setQuery] = useState('');
    const [selectedIndex, setSelectedIndex] = useState(0);
    const inputRef = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (isOpen) {
            inputRef.current?.focus();
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'unset';
        }
    }, [isOpen]);

    const results = useMemo(() => {
        if (!query.trim()) return [];
        return searchData.filter(item =>
            item.title.toLowerCase().includes(query.toLowerCase()) ||
            item.content.toLowerCase().includes(query.toLowerCase()) ||
            item.category.toLowerCase().includes(query.toLowerCase())
        ).slice(0, 6);
    }, [query]);


    const handleKeyDown = (e) => {
        if (e.key === 'ArrowDown') {
            setSelectedIndex(prev => (prev + 1) % results.length);
        } else if (e.key === 'ArrowUp') {
            setSelectedIndex(prev => (prev - 1 + results.length) % results.length);
        } else if (e.key === 'Enter' && results.length > 0) {
            handleSelect(results[selectedIndex]);
        } else if (e.key === 'Escape') {
            onClose();
        }
    };

    const handleSelect = (item) => {
        navigate(item.link);
        onClose();
        setQuery('');
    };

    const getCategoryIcon = (category) => {
        switch (category) {
            case 'Chipset': return <Cpu className="w-4 h-4" />;
            case 'Error': return <AlertTriangle className="w-4 h-4" />;
            case 'Guide': return <FileText className="w-4 h-4" />;
            case 'FAQ': return <MessageCircle className="w-4 h-4" />;
            default: return <FileText className="w-4 h-4" />;
        }
    };

    return (
        <AnimatePresence>
            {isOpen && (
                <>
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        onClick={onClose}
                        className="fixed inset-0 bg-white/40 dark:bg-black/60 backdrop-blur-sm z-[100]"
                    />
                    <motion.div
                        initial={{ opacity: 0, scale: 0.95, y: -20 }}
                        animate={{ opacity: 1, scale: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.95, y: -20 }}
                        className="fixed top-[15%] left-1/2 -translate-x-1/2 w-full max-w-2xl z-[101] px-4"
                    >
                        <div className="glass rounded-[2rem] border-black/5 dark:border-white/10 shadow-2xl overflow-hidden">
                            <div className="p-6 border-b border-black/5 dark:border-white/5 flex items-center gap-4 bg-white dark:bg-transparent">
                                <SearchIcon className="text-tcl-red w-6 h-6" />
                                <input
                                    ref={inputRef}
                                    type="text"
                                    placeholder="Search chipsets, guides, errors..."
                                    className="bg-transparent border-none outline-none text-gray-900 dark:text-white text-xl w-full placeholder:text-gray-500 font-medium"
                                    value={query}
                                    onChange={(e) => {
                                        setQuery(e.target.value);
                                        setSelectedIndex(0);
                                    }}
                                    onKeyDown={handleKeyDown}
                                />
                                <div className="flex items-center gap-2">
                                    <div className="hidden sm:flex items-center gap-1 px-2 py-1 rounded bg-white/5 border border-white/10 text-[10px] text-gray-400 font-bold">
                                        <Command size={10} /> K
                                    </div>
                                    <button onClick={onClose} className="p-2 hover:bg-white/5 rounded-xl transition-colors">
                                        <X className="text-gray-500 w-5 h-5" />
                                    </button>
                                </div>
                            </div>

                            <div className="max-h-[400px] overflow-y-auto p-4 custom-scrollbar">
                                {results.length > 0 ? (
                                    <div className="space-y-2">
                                        {results.map((item, index) => (
                                            <div
                                                key={item.id}
                                                onMouseEnter={() => setSelectedIndex(index)}
                                                onClick={() => handleSelect(item)}
                                                className={`p-4 rounded-2xl flex items-center justify-between cursor-pointer transition-all ${selectedIndex === index ? 'bg-tcl-red/10 border-tcl-red/20 ring-1 ring-tcl-red/30' : 'border-transparent'
                                                    } border`}
                                            >
                                                <div className="flex items-center gap-4">
                                                    <div className={`w-10 h-10 rounded-xl flex items-center justify-center ${selectedIndex === index ? 'bg-tcl-red text-white' : 'bg-black/5 dark:bg-white/5 text-gray-500 dark:text-gray-400'
                                                        }`}>
                                                        {getCategoryIcon(item.category)}
                                                    </div>
                                                    <div>
                                                        <div className="flex items-center gap-2 mb-1">
                                                            <span className="text-gray-900 dark:text-white font-bold">{item.title}</span>
                                                            <span className="text-[10px] uppercase font-black tracking-widest text-tcl-red/60">{item.category}</span>
                                                        </div>
                                                        <p className="text-sm text-gray-400 line-clamp-1">{item.content}</p>
                                                    </div>
                                                </div>
                                                {selectedIndex === index && (
                                                    <div className="flex items-center gap-2 text-tcl-red font-bold text-xs uppercase tracking-widest animate-in fade-in slide-in-from-right-2">
                                                        Go <CornerDownLeft size={14} />
                                                    </div>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                ) : query.trim() ? (
                                    <div className="py-12 text-center">
                                        <div className="text-gray-500 font-medium mb-2">No results found for "{query}"</div>
                                        <div className="text-xs text-gray-600 uppercase font-black tracking-widest">Try searching for MT9615, OTA, or Wipes</div>
                                    </div>
                                ) : (
                                    <div className="py-8 px-4">
                                        <div className="text-[10px] font-black text-gray-500 uppercase tracking-widest mb-6">Popular Searches</div>
                                        <div className="grid grid-cols-2 gap-3 text-sm">
                                            {['MT9615', 'RT51', 'USB Prep', 'Verification Failed'].map(pop => (
                                                <button
                                                    key={pop}
                                                    onClick={() => setQuery(pop)}
                                                    className="p-3 rounded-xl border border-black/5 dark:border-white/5 hover:border-tcl-red/20 hover:bg-black/5 dark:hover:bg-white/5 text-left text-gray-500 dark:text-gray-400 transition-all font-medium"
                                                >
                                                    {pop}
                                                </button>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>

                            <div className="p-4 border-t border-black/5 dark:border-white/5 bg-gray-50 dark:bg-black/40 flex items-center justify-between">
                                <div className="flex gap-6">
                                    <div className="flex items-center gap-2">
                                        <div className="p-1 rounded bg-white/5 border border-white/10 text-[10px] text-gray-400">
                                            <ArrowRight className="w-2.5 h-2.5 rotate-90" />
                                        </div>
                                        <span className="text-[10px] text-gray-500 font-bold uppercase tracking-widest">Navigate</span>
                                    </div>
                                    <div className="flex items-center gap-2">
                                        <div className="px-1.5 py-0.5 rounded bg-white/5 border border-white/10 text-[10px] text-gray-400">
                                            Enter
                                        </div>
                                        <span className="text-[10px] text-gray-500 font-bold uppercase tracking-widest">Select</span>
                                    </div>
                                </div>
                                <div className="text-[10px] text-tcl-red/40 font-black uppercase tracking-widest">TCL Hub Search</div>
                            </div>
                        </div>
                    </motion.div>
                </>
            )}
        </AnimatePresence>
    );
};

export default Search;
