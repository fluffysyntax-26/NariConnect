import React from 'react';
import { Menu, X } from 'lucide-react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { SignedIn, SignedOut, UserButton } from '@clerk/clerk-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = React.useState(false);
  const navigate = useNavigate();

  return (
    <nav className="fixed w-full bg-white/80 backdrop-blur-md z-50 border-b border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <div className="flex-shrink-0 flex items-center cursor-pointer" onClick={() => navigate('/')}>
            <span className="text-2xl font-bold bg-gradient-to-r from-rose-500 to-pink-600 bg-clip-text text-transparent">
              NariConnect
            </span>
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            <SignedOut>
              <div className="flex items-center space-x-4">
                <button 
                  onClick={() => navigate('/sign-in')}
                  className="text-gray-600 hover:text-rose-500 font-medium transition-colors"
                >
                  Log In
                </button>
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => navigate('/sign-up')}
                  className="bg-rose-500 text-white px-6 py-2 rounded-full font-medium hover:bg-rose-600 transition-colors shadow-lg shadow-rose-500/30"
                >
                  Sign Up
                </motion.button>
              </div>
            </SignedOut>

            <SignedIn>
              <div className="flex items-center space-x-4">
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => navigate('/dashboard')}
                  className="text-gray-600 hover:text-rose-500 font-medium transition-colors"
                >
                  Dashboard
                </motion.button>
                <UserButton afterSignOutUrl="/" />
              </div>
            </SignedIn>
          </div>

          <div className="md:hidden flex items-center">
            <button onClick={() => setIsOpen(!isOpen)} className="text-gray-600">
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      {isOpen && (
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="md:hidden bg-white border-b border-gray-100"
        >
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            <SignedOut>
              <button 
                onClick={() => navigate('/sign-in')}
                className="block w-full text-left px-3 py-2 text-gray-600 hover:text-rose-500 font-medium"
              >
                Log In
              </button>
              <button 
                onClick={() => navigate('/sign-up')}
                className="block w-full text-left px-3 py-2 text-rose-500 font-bold"
              >
                Sign Up
              </button>
            </SignedOut>

            <SignedIn>
              <button 
                onClick={() => navigate('/dashboard')}
                className="block w-full text-left px-3 py-2 text-rose-500 font-bold"
              >
                Go to Dashboard
              </button>
              <div className="px-3 py-2">
                <UserButton afterSignOutUrl="/" />
              </div>
            </SignedIn>
          </div>
        </motion.div>
      )}
    </nav>
  );
};

export default Navbar;
