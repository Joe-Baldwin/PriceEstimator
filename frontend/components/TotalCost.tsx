import React from 'react';

type Item = { msrp_price: number };

type Props = {
  items: Item[];
};

const TotalCost: React.FC<Props> = ({ items }) => {
  const total = items.filter(Boolean).reduce((sum, item) => sum + (typeof item.msrp_price === 'number' ? item.msrp_price : 0), 0);
  return (
    <div className="mt-4 text-xl font-bold text-right">
      Total MSRP: ${total.toFixed(2)}
    </div>
  );
};

export default TotalCost;
