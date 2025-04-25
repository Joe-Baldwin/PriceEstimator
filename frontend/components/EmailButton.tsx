import React from 'react';

type Props = {
  disabled: boolean;
  onClick: () => void;
};

const EmailButton: React.FC<Props> = ({ disabled, onClick }) => (
  <button
    className={`px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50 mr-2`}
    disabled={disabled}
    onClick={onClick}
  >
    Email Estimate
  </button>
);

export default EmailButton;
