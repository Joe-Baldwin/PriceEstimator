import React from 'react';

type Props = {
  disabled: boolean;
  onClick: () => void;
};

const ExportButton: React.FC<Props> = ({ disabled, onClick }) => (
  <button
    className={`px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50`}
    disabled={disabled}
    onClick={onClick}
  >
    Export to Excel
  </button>
);

export default ExportButton;
